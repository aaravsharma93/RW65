from yard.models import Barrier, TrafficLight, PriceGroup, ContainerShow, Io, ExternalWeigh, AutoCapture, \
    FirstWeightCameras, SecondWeightCameras


def barrier(request):
    barrier = Barrier.objects.all().last()
    count = []
    if barrier:
        if barrier.count:
            for i in range(barrier.count):
                count.append(i + 1)

    ampel = TrafficLight.objects.all().last()
    price = PriceGroup.objects.all().last()
    contr = ContainerShow.objects.all().last()
    io = Io.objects.all().last()
    ew = ExternalWeigh.objects.all().last()
    ac = AutoCapture.objects.all().last()
    fw = FirstWeightCameras.objects.all().last()
    sw = SecondWeightCameras.objects.all().last()
    return {
        'schrank': barrier,
        'count': count,
        'ampel':ampel,
        'p_group':price,
        'contr':contr,
        'i_o':io,
        'ew':ew,
        'ac':ac,
        'fw':fw,
        'sw':sw
        }
