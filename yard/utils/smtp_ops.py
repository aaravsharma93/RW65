import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def test_smtp_connection(data):
    session = smtplib.SMTP(data["host"], data["port"])
    session.starttls()
    session.login(data["username"], data["password"])
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You '''
    message = MIMEMultipart()
    message['From'] = data["username"]
    message['To'] = data["username"]
    message.attach(MIMEText(mail_content, 'plain'))
    text = message.as_string()
    session.sendmail(data["sender_address"], {data["sender_address"], }, text)
    session.quit()
    print('Mail Sent')


def send_mail(smtp_obj, message, receiver_mails):
    session = None
    try:
        session = smtplib.SMTP(smtp_obj.host, smtp_obj.port)
        session.starttls()
        session.login(smtp_obj.username, smtp_obj.password)
        session.sendmail(smtp_obj.sender_address, receiver_mails, message)
    except Exception as e:
        raise Exception(str(e))
    finally:
        if session is not None:
            session.quit()

    return "Send Mail"