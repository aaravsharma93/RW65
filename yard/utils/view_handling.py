import base64
import io
import json

import pyqrcode
import xlwt
from django.core.serializers import serialize
from django.shortcuts import redirect
from django.utils.translation import activate, get_language
from PIL import Image
from yard.models import Settings, images_base64, Customer, Vehicle, Forwarders, Supplier, Article, Combination, \
    SelectCamera, Logo, Container
from django.core.files.uploadedfile import InMemoryUploadedFile


def create_excel(data):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Lieferschein')
    row_num = 0
    columns = ['Lfd Nr', 'Kennz.1', 'kennz.2', 'Artikel', 'Kunde', 'Lieferant', 'Erst - Gewicht',
               'Zweit - Gewicht', 'Nettogewicht', 'Gesamtpreis', 'Alibi Nr.', 'Erzeugt am']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    values = data.values_list('id', 'vehicle__license_plate', 'vehicle__license_plate2', 'article__name',
                              'customer__name1', 'supplier__supplier_name', str('first_weight'),
                              str('second_weight'), str('net_weight'), 'total_price', 'secondw_alibi_nr',
                              'updated_date_time')

    for row in values:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 11:
                ws.write(row_num, col_num, row[col_num].isoformat())
            else:
                ws.write(row_num, col_num, row[col_num])
    return wb


def set_cxt(request):
    customer_list = json.loads(serialize('json', Customer.objects.all(), fields=('name1', 'pk')))
    vehicle_list = json.loads(serialize('json', Vehicle.objects.all(), fields=('license_plate', 'pk')))
    forwarder_list = json.loads(serialize('json', Forwarders.objects.all(), fields=('name', 'pk')))
    article_list = json.loads(
        serialize('json', Article.objects.filter(yard=request.user.yard), fields=('name', 'pk')))
    supplier_list = json.loads(serialize('json', Supplier.objects.all(), fields=('supplier_name', 'pk')))
    combination_list = json.loads(serialize('json', Combination.objects.all(), fields=('ident', 'pk')))
    container_list = json.loads(serialize('json', Container.objects.all(), fields=('name', 'pk')))
    camera = SelectCamera.objects.all().last()
    logo = Logo.objects.all()
    set_settings_session(request)
    context = {"customer_list": customer_list, "vehicle_list": vehicle_list, "article_list": article_list,
               "supplier_list": supplier_list, "combination_list": combination_list, "container_list": container_list,
               "forwarder_list": forwarder_list, "language": get_language(), "camera": camera, 'logo': logo}
    return context


def set_ss_cxt(request):
    user = request.user
    customer_list = json.loads(serialize('json', user.customer_set.all(), fields=('name1', 'pk')))
    vehicle_list = json.loads(serialize('json', user.vehicle_set.all(), fields=('license_plate', 'pk')))
    forwarder_list = json.loads(serialize('json', Forwarders.objects.all(), fields=('name', 'pk')))
    article_list = json.loads(
        serialize('json', user.article_set.filter(yard=request.user.yard), fields=('name', 'pk')))
    supplier_list = json.loads(serialize('json', user.supplier_set.all(), fields=('supplier_name', 'pk')))
    combination_list = json.loads(serialize('json', Combination.objects.all(), fields=('ident', 'pk')))
    container_list = json.loads(serialize('json', Container.objects.all(), fields=('name', 'pk')))
    camera = SelectCamera.objects.all().last()
    logo = Logo.objects.all()
    set_settings_session(request)
    context = {"customer_list": customer_list, "vehicle_list": vehicle_list, "article_list": article_list,
               "supplier_list": supplier_list, "combination_list": combination_list, "container_list": container_list,
               "forwarder_list": forwarder_list, "language": get_language(), "camera": camera, 'logo': logo}
    return context


def generate_qr_code(url):
    url = pyqrcode.create(url)
    # url.svg('uca.svg', scale=4)
    buffer = io.BytesIO()
    text_obj = url.png_as_base64_str()
    # byte_str = buffer.getvalue()
    # text_obj = byte_str.decode('UTF-8')
    return text_obj


def get_images(image_base64, trans_id, index):
    try:
        data = base64.b64decode(image_base64.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        img_io = io.BytesIO()
        img.save(img_io, format='JPEG')
        return InMemoryUploadedFile(img_io, field_name=None, name=f"img_{trans_id}_{index}.jpg",
                                    content_type='image/jpeg', size=img_io.tell, charset=None)
    except Exception as e:
        print(e)
        return None


def save_base64(request, trans_id):
    try:
        img1 = get_images(request.POST.get('image_loading1'), trans_id, 1)
        img2 = get_images(request.POST.get('image_loading2'), trans_id, 2)
        img3 = get_images(request.POST.get('image_loading3'), trans_id, 3)
        img_obj, create = images_base64.objects.update_or_create(transaction_id=trans_id,
                                                                 defaults={"image1": img1, "image2": img2,
                                                                           "image3": img3})
        # img_obj,create = images_base64.objects.update_or_create(transaction_id = trans_id, image1 = img1, image2 = img2, image3 = img3)
        img_obj.save()
    except Exception as e:
        print("error occured  during save base64 : ", e)


def set_settings_session(request):
    try:
        settings = Settings.objects.all()[0]
        request.session["customer"] = settings.customer
        request.session["supplier"] = settings.supplier
        request.session["article"] = settings.article
        request.session["show_article"] = settings.show_article
        request.session["show_supplier"] = settings.show_supplier
        request.session["show_yard"] = settings.show_yard
        request.session["show_forwarders"] = settings.show_forwarders
        request.session["show_storage"] = settings.show_storage
        request.session["show_building_site"] = settings.show_building_site
        request.session["read_number_from_camera"] = settings.read_number_from_camera
        request.session["language"] = settings.language
        activate(settings.language)
    except:
        pass


# this code is used for changing the language
def changelanguage(request, lang):
    print(lang)
    # print(get_language())
    activate(lang)
    return redirect('/')


def yard_check(user):
    return user.yard is not None


def user_role(user):
    if user.role != "operator":
        return True
    else:
        return False
