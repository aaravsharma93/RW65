# runapscheduler.py
import logging

from django.conf import settings
from agri.models import Weather, Location
import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)


def my_job():
    # Your job processing logic here...
    loc = Location.objects.all()
    for j in loc:
        lat = j.long_lat[0]["lat"]
        lng = j.long_lat[0]["lng"]
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=current,minutely,hourly&units=metric&appid=21e696f4e0e757c95340595f106183b3"
        rs = requests.get(url)
        data = rs.json()

        day_temp = data["daily"][0]["temp"]["day"]
        min_temp = data["daily"][0]["temp"]["min"]
        max_temp = data["daily"][0]["temp"]["max"]
        night_temp = data["daily"][0]["temp"]["night"]
        eve_temp = data["daily"][0]["temp"]["eve"]
        morn_temp = data["daily"][0]["temp"]["morn"]
        pressure = data["daily"][0]["pressure"]
        humidity = data["daily"][0]["humidity"]
        dew_point = data["daily"][0]["dew_point"]
        pressure = data["daily"][0]["pressure"]
        description = data["daily"][0]["weather"][0]["description"]
        clouds = data["daily"][0]["clouds"]

        w = Weather.objects.create(location=j)
        w.day_temp = day_temp
        w.min_temp = min_temp
        w.max_temp = max_temp
        w.night_temp = night_temp
        w.morn_temp = morn_temp
        w.pressure = pressure
        w.evn_temp = eve_temp
        w.dew_point = dew_point
        w.humidity = humidity
        w.description = description
        w.eve_temp = eve_temp
        w.clouds = clouds
        if "rain" in data["daily"][0]:
            rain = data["daily"][0]["rain"]
            w.rain = rain
        w.save()
        time.sleep(10)
    print("Today Weather Added")


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after our job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day="*/1"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
