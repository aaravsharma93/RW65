import base64
import json
import os
import re
from io import BytesIO
from urllib import parse as urlparse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.base import ContentFile
from django.core.serializers import serialize
from django.db.models import Sum
from django.forms import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.views import View
from xhtml2pdf import pisa

from yard.forms import WarehouseForm, SmtpForm, SettingsForm, VehicleForm, CustomerForm, ForwardersForm, SupplierForm, \
                        ContractForm, SiloForm, MaterialQualityForm
from yard.models import Logo, Vehicle, Forwarders, Signature, Combination, Warehouse, SMTPCred, SelectCamera, Barrier, \
                        Settings, Customer, Supplier, TrafficLight, PriceGroup, ContainerShow, ShowTonne, Io, ExternalWeigh, ForeignWeigh, \
                        Contract, Article, BuildingSite, AutoCapture, FirstWeightCameras, SecondWeightCameras, Transaction, Silo, \
                        MaterialQuality
from django.contrib import messages

from yard.render import link_callback
from yard.utils.view_handling import yard_check, set_settings_session, user_role, generate_qr_code
from yardman.settings import BASE_DIR


def schrank(request):
    return render(request, "yard/schrank.html")


def copy(request):
    if 'down' in request.POST:
        file = open('Copyright.pdf', 'rb')
        response = HttpResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Urheberrecht.pdf"'
        return response
    return render(request, "yard/copyright.html")


# API for loading details from ajax to editform
@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def combination(request, identifier):
    try:
        obj = Combination.objects.get(id=identifier)

    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    # data.update(foreign_data)
    else:
        data = {}
    return JsonResponse(data)


""" Customer Views """


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def customer(request):
    context = {}
    form = CustomerForm(request.POST or None)
    if request.POST:
        idd = request.POST.get('id')
        try:
            obj = Customer.objects.get(id=idd)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = CustomerForm(None)
            context['form'] = form
            context["dataset"] = Customer.objects.all()
            return render(request, "yard/customer-2.html", context)
        ##to handle update TBD
        form = CustomerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = CustomerForm(None)
        context["form"] = form
        context["dataset"] = Customer.objects.all()
        return render(request, "yard/customer-2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Customer.objects.all()
        return render(request, "yard/customer-2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def customer_details(request, identifier):
    try:
        obj = Customer.objects.get(id=identifier)
    except Exception as e:
        print(e)
        obj = None
    if obj:
        data = model_to_dict(obj)
        del data["ss_role_access"]
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def customer_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Customer, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/customer")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def customer_list(request):
    # if request.is_ajax():
    queryset = json.loads(serialize('json', Customer.objects.all()))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


"""  vehicle data view """


@login_required(redirect_field_name=None)  ##@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def vehicle(request):
    context = {}
    form = VehicleForm(request.POST or None)
    if request.POST:
        id = request.POST.get('id')
        try:
            obj = Vehicle.objects.get(id=id)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = VehicleForm(None)
            context['form'] = form
            context["dataset"] = Vehicle.objects.all()
            return render(request, "yard/vehicle2.html", context)
        ##to handle update TBD
        form = VehicleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = VehicleForm(None)
        context["form"] = form
        context["dataset"] = Vehicle.objects.all()
        return render(request, "yard/vehicle2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Vehicle.objects.all()
        return render(request, "yard/vehicle2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def vehicle_detail(request, identifier):
    try:
        obj = Vehicle.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        vehicle_weight_date = {"updated_date_time": obj.updated_date_time}
        data = model_to_dict(obj)
        del data["ss_role_access"]
        data.update(vehicle_weight_date)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def vehicle_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Vehicle, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/vehicle")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def vehicle_list(request):
    # if request.is_ajax():
    queryset = json.loads(serialize('json', Vehicle.objects.all()))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


""" Forwarders View """


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def forwarders(request):
    context = {}
    form = ForwardersForm(request.POST or None)

    if request.POST:
        idd = request.POST.get('id')
        try:
            obj = Forwarders.objects.get(id=idd)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = ForwardersForm(None)
            else:
                print("Form not valid")
            context['form'] = form
            context["dataset"] = Forwarders.objects.all()
            return render(request, "yard/forwarders2.html", context)
        ##to handle update TBD
        form = ForwardersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = ForwardersForm(None)
        context["form"] = form
        context["dataset"] = Forwarders.objects.all()
        return render(request, "yard/forwarders2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Forwarders.objects.all()
        return render(request, "yard/forwarders2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def forwarders_detail(request, identifier):
    try:
        obj = Forwarders.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def forwarders_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Forwarders, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/forwarders")


""" Supplier View """


# @staff_member_required
@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def supplier(request):
    context = {}
    form = SupplierForm(request.POST or None)

    if request.POST:
        idd = request.POST.get('id')
        try:
            obj = Supplier.objects.get(id=idd)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = SupplierForm(None)
            context['form'] = form
            context["dataset"] = Supplier.objects.all()
            return render(request, "yard/supplier2.html", context)
        ##to handle update TBD
        form = SupplierForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = SupplierForm(None)
        context["form"] = form
        context["dataset"] = Supplier.objects.all()
        return render(request, "yard/supplier2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Supplier.objects.all()
        return render(request, "yard/supplier2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def supplier_detail(request, identifier):
    try:
        obj = Supplier.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
        del data["ss_role_access"]

    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def supplier_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Supplier, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/supplier")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def supplier_list(request):
    # if request.is_ajax():
    queryset = json.loads(serialize('json', Supplier.objects.all()))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


def logo(request):
    if request.POST:
        try:
            model = Logo.objects.get(id=1)
        except:
            model = None
        if "save_logo" in request.POST:
            img = request.FILES.get('logo')
            if img is not None:
                ext = img.name.split('.')[-1].lower()
            else:
                messages.error(request, "There is no Logo to Update")
                return HttpResponseRedirect('/settings')
            if ext != 'png' and ext != 'jpg' and ext != 'jpeg':
                messages.error(request, "Please Upload a valid png or jpg file")
                return HttpResponseRedirect('/settings')
            if model is not None:
                model.logo = img
                model.save()
                messages.success(request, "Logo Updated")
            else:
                logo = Logo(logo=img)
                logo.save()
                messages.success(request, "Data Added")
        if "save_heading" in request.POST:
            head = request.POST.get('heading')
            if head is not None:
                if model is not None:
                    model.heading = head.lstrip()
                    model.save()
                    messages.success(request, "Heading Updated")
                else:
                    logo = Logo(heading=head)
                    logo.save()
                    messages.success(request, "New Heading Added")
            else:
                messages.error(request, "No Heading to update")

    return HttpResponseRedirect('/settings')


def vehicle_save(request):
    licen_plt = request.GET.get('licence_plate')
    licen_plt2 = request.GET.get('licence_plate2')
    weight = request.GET.get('weight')
    forwarder = request.GET.get('forwarder')
    try:
        try:
            if re.match('^[0-9]*$', licen_plt):
                try:
                    vehicle = Vehicle.objects.get(id=licen_plt)
                except:
                    vehicle = Vehicle.objects.get(license_plate=licen_plt)
            else:
                vehicle = Vehicle.objects.get(license_plate=licen_plt)
        except:
            vehicle = Vehicle.objects.create(license_plate=licen_plt)
        try:
            vehicle.forwarder = Forwarders.objects.get(id=forwarder)
        except:
            pass

        from datetime import datetime
        nowd = datetime.now()
        date = nowd.strftime('%Y-%m-%d')
        time = nowd.strftime('%H:%M:%S')
        vehicle.vehicle_weight_date = date
        vehicle.vehicle_weight_time = time
        vehicle.vehicle_weight = weight
        vehicle.license_plate2 = licen_plt2
        vehicle.save()
        return JsonResponse({'status': 1})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 0})


def sign(request):
    if request.POST:
        sign = request.FILES.get('signature')
        if sign is None:
            messages.error(request, "No signature to save")
            return HttpResponseRedirect('/user_edit')
        try:
            obj, created = Signature.objects.update_or_create(user=request.user, signature=sign)
            obj.save()
            messages.success(request, "Signature Saved")
        except:
            messages.error(request, "Error occurred")

        return HttpResponseRedirect('/user_edit')
    else:
        return HttpResponseRedirect('/user_edit')


def comb_list(request):
    data = Combination.objects.all()
    return render(request, "yard/id.html", {'data': data})


def comb_delete(request, identifier):
    obj = get_object_or_404(Combination, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/comb_list")


def advance_set(request):
    if 'clear' in request.POST:
        request.session['perm'] = False

    code = request.session.get('code')
    permission = request.session.get('perm', False)
    password = request.POST.get('login_password')

    if not request.POST and permission == False:
        import random
        lst = []
        for i in range(8):
            lst.append(random.randint(2, 9))
        request.session['code'] = "".join([str(x) for x in lst])

    if code is not None:
        from datetime import date
        passcode = date.today().strftime('%d%m%Y')

    if password is not None and password != '':
        if password == passcode:
            request.session['perm'] = True
        else:
            request.session['perm'] = False
            messages.error(request, "Enter Password")

    if request.session.get('perm'):
        context = {}
        try:
            if request.POST.get('check_yes') is not None:
                SelectCamera.objects.all().delete()
                camera = SelectCamera(yes=True, number=int(request.POST.get('total_camera')))
                camera.save()
            if request.POST.get('check_No') is not None:
                SelectCamera.objects.all().delete()
                camera = SelectCamera(yes=False)
                camera.save()
            if request.POST.get('schrank_yes') is not None:
                Barrier.objects.all().delete()
                bar = Barrier(barrier=True)
                bar.save()
            if request.POST.get('schrank_no') is not None:
                Barrier.objects.all().delete()
                bar = Barrier(barrier=False)
                bar.save()
            if request.POST.get('tl_yes') is not None:
                TrafficLight.objects.all().delete()
                tl = TrafficLight(status=True)
                tl.save()
            if request.POST.get('tl_no') is not None:
                TrafficLight.objects.all().delete()
                tl = TrafficLight(status=False)
                tl.save()
        except Exception as e:
            print(e)
            pass
        context["camera"] = SelectCamera.objects.all().last()

        context["barr"] = Barrier.objects.all().last()
        context["ampel"] = TrafficLight.objects.all().last()

        return render(request, "yard/settings_advance.html", context)
    else:
        return render(request, "yard/perm.html")


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
@user_passes_test(user_role)
def settings(request):
    context = {}
    try:
        if request.POST.get('p_grp_y') is not None:
            PriceGroup.objects.all().delete()
            p = PriceGroup(status=True)
            p.save()
        if request.POST.get('p_grp_n') is not None:
            PriceGroup.objects.all().delete()
            p = PriceGroup(status=False)
            p.save()
        if request.POST.get('contr_y') is not None:
            ContainerShow.objects.all().delete()
            c = ContainerShow(status=True)
            c.save()
        if request.POST.get('contr_n') is not None:
            ContainerShow.objects.all().delete()
            c = ContainerShow(status=False)
            c.save()
        if request.POST.get('show_ty') is not None:
            ShowTonne.objects.all().delete()
            T = ShowTonne(status=True)
            T.save()
        if request.POST.get('show_tn') is not None:
            ShowTonne.objects.all().delete()
            T = ShowTonne(status=False)
            T.save()
        if request.POST.get('io_y') is not None:
            Io.objects.all().delete()
            I = Io(status=True)
            I.save()
        if request.POST.get('io_n') is not None:
            Io.objects.all().delete()
            I = Io(status=False)
            I.save()
        if request.POST.get('ew_y') is not None:
            ExternalWeigh.objects.all().delete()
            E = ExternalWeigh(status=True)
            E.save()
        if request.POST.get('ew_n') is not None:
            ExternalWeigh.objects.all().delete()
            E = ExternalWeigh(status=False)
            E.save()
        if request.POST.get('ac_y') is not None:
            AutoCapture.objects.all().delete()
            A = AutoCapture(status=True)
            A.save()
        if request.POST.get('ac_n') is not None:
            AutoCapture.objects.all().delete()
            A = AutoCapture(status=False)
            A.save()
    except Exception as e:
        print(e)
        pass
    try:
        obj = Settings.objects.all()[0]
    except Exception as e:
        obj = None
    if obj:
        form = SettingsForm(request.POST or None, instance=obj)
    else:
        form = SettingsForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            obj = form.instance
            obj.yard = request.user.yard
            smt_creds = SMTPCred.objects.get(id=request.POST["smtp_creds"]) if request.POST[
                                                                                   "smtp_creds"] != "" else None
            if smt_creds:
                obj.smtp_creds = smt_creds
            obj.save()
            form.save()
        else:
            return HttpResponse(form.errors, status=400)
    if obj:
        context["smtp_form"] = SmtpForm(instance=obj.smtp_creds)
    else:
        context["smtp_form"] = SmtpForm()
    set_settings_session(request)
    context["form"] = form
    context["heading"] = Logo.objects.all()
    context['price'] = PriceGroup.objects.all().last()
    context['contr'] = ContainerShow.objects.all().last()
    context['show_t'] = ShowTonne.objects.all().last()
    context['io'] = Io.objects.all().last()
    context['ew'] = ExternalWeigh.objects.all().last()
    context['ac'] = AutoCapture.objects.all().last()
    return render(request, "yard/settings2.html", context)


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def test_smtp_connection(request):
    if request.method == "POST":
        print(request.POST)
        try:
            test_smtp_connection(request.POST)
        except Exception as e:
            return HttpResponse(str(e), status=400)
        return HttpResponse("Good")
    return HttpResponse(status=404)


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def save_smtp_connection(request):
    if request.method == "POST":
        obj = SMTPCred.objects.first()
        if obj:
            form = SmtpForm(request.POST, instance=obj)
        else:
            form = SmtpForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return JsonResponse(model_to_dict(obj), status=200)
        else:
            return HttpResponse(form.errors, status=400)
    return HttpResponse(status=404)


def e_sign(request):
    if request.POST:
        data = request.POST.get('signature')
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
        sign = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        if sign is None:
            messages.error(request, "No signature to save")
            return HttpResponseRedirect('/user_edit')
        try:
            obj, created = Signature.objects.update_or_create(user=request.user, signature=sign)
            obj.save()
            messages.success(request, "Signature Saved")
        except:
            messages.error(request, "Error occurred")

        return HttpResponseRedirect('/user_edit')

    return render(request, "yard/e_sign.html")


def auto_capture(request):
    if request.POST:
        fw = {'cam_1': False, 'cam_2': False, 'cam_3': False}
        sw = {'cam_1': False, 'cam_2': False, 'cam_3': False}

        if request.POST.get('fw_cam_1') is not None:
            fw['cam_1'] = True
        if request.POST.get('fw_cam_2') is not None:
            fw['cam_2'] = True
        if request.POST.get('fw_cam_3') is not None:
            fw['cam_3'] = True
        if request.POST.get('sw_cam_1') is not None:
            sw['cam_1'] = True
        if request.POST.get('sw_cam_2') is not None:
            sw['cam_2'] = True
        if request.POST.get('sw_cam_3') is not None:
            sw['cam_3'] = True

        fw_cam_1 = request.POST.get('fw_cam_1')
        fw_cam_2 = request.POST.get('fw_cam_2')
        fw_cam_3 = request.POST.get('fw_cam_3')
        sw_cam_1 = request.POST.get('sw_cam_1')
        sw_cam_2 = request.POST.get('sw_cam_2')
        sw_cam_3 = request.POST.get('sw_cam_3')

        if fw_cam_1 is not None or fw_cam_2 is not None or fw_cam_3 is not None:
            FirstWeightCameras.objects.all().delete()
            F = FirstWeightCameras(cam1=fw['cam_1'], cam2=fw['cam_2'], cam3=fw['cam_3'])
            F.save()

        if sw_cam_1 is not None or sw_cam_2 is not None or sw_cam_3 is not None:
            SecondWeightCameras.objects.all().delete()
            S = SecondWeightCameras(cam1=sw['cam_1'], cam2=sw['cam_2'], cam3=sw['cam_3'])
            S.save()

        return redirect('/settings')

    context = {}
    context['fw'] = FirstWeightCameras.objects.all().last()
    context['sw'] = SecondWeightCameras.objects.all().last()
    return render(request, "yard/automatic_capture.html", context)


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def warehouse(request):
    context = {}
    form = WarehouseForm(request.POST or None)

    if request.POST:
        id = request.POST.get('id')
        try:
            obj = Warehouse.objects.get(id=id)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = WarehouseForm(None)
            context['form'] = form
            context["dataset"] = Warehouse.objects.all()
            # context["art_meta"] = Article_meta.objects.all()
            return render(request, "yard/warehouse.html", context)
        ##to handle update TBD
        form = WarehouseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = WarehouseForm(None)
        context["form"] = form
        context["dataset"] = Warehouse.objects.all()
        return render(request, "yard/warehouse.html", context)
    else:
        context["form"] = form
        context["dataset"] = Warehouse.objects.all()
        return render(request, "yard/warehouse.html", context)


@login_required
def warehouse_detail(request, identifier):
    try:
        obj = Warehouse.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def warehouse_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Warehouse, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/warehouse")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def warehouse_list(request):
    # if request.is_ajax():
    # queryset = json.loads(serialize('json', Article.objects.all()))
    queryset = json.loads(serialize('json', Warehouse.objects.all()))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


def foreign_list(request, id=None):
    if id is not None:
        obj = get_object_or_404(ForeignWeigh, id=id)
        obj.delete()
        return HttpResponseRedirect("/foreign_list")
    else:
        context = {}
        context['dataset'] = ForeignWeigh.objects.all()
        return render(request, "yard/foreign.html", context)


# Contract View

def get_contract(request, contract_number):
    if request.method == "GET":
        try:
            obj = Contract.objects.get(contract_number=contract_number)
            material_list = []
            for mat in obj.required_materials:
                article = Article.objects.get(id=mat["material"])
                article_obj = {
                    "id":article.id,
                    "name":article.name
                }
                materials_obj = {
                    "material": article_obj,
                    "agreed_value": mat["agreed_value"],
                    "remaining": sum(Transaction.objects.filter(article_id=mat["material"], customer=contract.customer)
                                     .values_list("net_weight", flat=True))
                }
                material_list.append(materials_obj)
            return JsonResponse({
                "contract_number": obj.contract_number,
                "customer": obj.customer.id,
                "article": obj.article.id,
                "agreed_value": obj.agreed_value,
                "vehicles": [i[0] for i in obj.vehicles.all().values_list("id")],
                "construction_site": [i[0] for i in obj.construction_site.all().values_list("id")]
            })
        except Contract.DoesNotExist as e:
            return HttpResponse(status=404)
        pass
    else:
        return HttpResponse(status=405)


def contract_pdf(request, contract_number):
    if request.method == "GET":
        obj = Contract.objects.get(contract_number=contract_number)
        url = request.build_absolute_uri(f"/contract_pdf/{obj.contract_number}")
        svg_value = generate_qr_code(url)
        ctx = {
            "contract": obj,
            "vehicles": ",".join([i.license_plate for i in obj.vehicles.all()]),
            "construction_site": ",".join([i.name for i in obj.construction_site.all()]),
            "qr_code": svg_value
        }
        template = get_template("yard/contract_pdf_template.html")
        html = template.render(ctx)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response, link_callback=link_callback)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
        # return render(request, "yard/contract_pdf_template.html", ctx)
    else:
        return HttpResponse(status=405)


def update_contract(request):
    form = ContractForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse(form.errors, status=400)


class ContractView(View):

    def get(self, request):
        ctx = {}
        contracts = Contract.objects.all()
        contract_list = []
        for contract in contracts:
            material_list = []
            for mat in contract.required_materials:
                materials_obj = {
                    "material": Article.objects.get(id=mat["material"]),
                    "agreed_value": mat["agreed_value"],
                    "remaining": sum(Transaction.objects.filter(article__id=mat["material"], customer=contract.customer)
                                     .values_list("net_weight", flat=True))
                }
                material_list.append(materials_obj)
            contract_obj = {
                "contract_number": contract.contract_number,
                "customer": contract.customer,
                "materials": material_list,
                "construction_site": contract.construction_site,
                "signature": contract.signature,
                "start_date": contract.start_date,
                "end_date": contract.end_date
            }
            contract_list.append(contract_obj)

        ctx["contracts"] = contract_list
        ctx["contract_form"] = ContractForm()
        ctx["customers"] = Customer.objects.all()
        ctx["materials"] = Article.objects.all()
        ctx["vehicles"] = Vehicle.objects.all()
        ctx["construction_sites"] = BuildingSite.objects.all()
        return render(request, "yard/contracts.html", context=ctx)

    def post(self, request):
        data = json.loads(request.body)
        form = ContractForm(data=data)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse(form.errors, status=400)

    def put(self, request):
        data = json.loads(request.body)
        try:
            obj = Contract.objects.get(contract_number=data["contract_number"])
        except Contract.DoesNotExist as e:
            return JsonResponse({"status": "Not Found"}, status=404)

        form = ContractForm(data=data, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})

        else:
            return JsonResponse(form.errors, status=400)

class Silo_view(View):

    def get(self, request):
        context = {}
        context['dataset'] = Silo.objects.all()
        context['form'] = SiloForm()
        return render(request, "yard/silo.html",context)
    
    def post(self, request):
        form = SiloForm(request.POST)
        if form.is_valid():
            form.save()
        context = {}
        context['dataset'] = Silo.objects.all()
        context['form'] = SiloForm()
        return render(request, "yard/silo.html",context)
    
def material_quality(request,_id):
    context = {}
    if request.POST:
        count = request.POST['count']
        if int(count) > 0:
            for i in range(int(count)):
                humidity = request.POST.get('humidity'+str(i))
                quality = request.POST.get('quality'+str(i))
                material = request.POST.get('material')
                amount = request.POST.get('Amount'+str(i))
                fertilizer = request.POST.get('fertilizer'+str(i))
                art = Article.objects.get(id=int(material))
                obj = MaterialQuality.objects.create(material=art, quality=quality, humidity=humidity, Amount=amount, Fertilizer=fertilizer)
                obj.save()
        return HttpResponseRedirect('/article')

    data = MaterialQuality.objects.filter(material=_id)
    if len(data) > 0:
        context['form'] = MaterialQualityForm(data=data)
    else:
        context['form'] = MaterialQualityForm()
    context['id'] = _id
    context['data'] = data
    return render(request, 'yard/art_quality.html', context)

def material_quality_delete(request):
    id = request.GET['id']
    obj = MaterialQuality.objects.get(id=id)
    obj.delete()
    return JsonResponse({'status':1})

def schlag_detail(request, _id):
    context = {}
    if request.POST:
        count = request.POST['count']
        if int(count) > 0:
            for i in range(int(count)):
                humidity = request.POST.get('humidity'+str(i))
                quality = request.POST.get('quality'+str(i))
                material = request.POST.get('material'+str(i))
                amount = request.POST.get('Amount'+str(i))
                fertilizer = request.POST.get('fertilizer'+str(i))
                art = Article.objects.get(id=int(material))
                obj = MaterialQuality.objects.create(material=art, quality=quality, humidity=humidity, Amount=amount, Fertilizer=fertilizer)
                obj.save()
        return HttpResponseRedirect('/supplier')

    art = Article.objects.filter(supplier__id=_id)
    lst = []
    for article in art:
        mat = MaterialQuality.objects.filter(material=article.id)
        if len(mat) > 0:
            lst.append(mat)

    count = [i+1 for i in range(mat.count())]
    context['id'] = _id
    context['article'] = art
    context['data'] = lst

    return render(request, "yard/schlag_detail.html", context)

def sclag_delete(request):
    id = request.GET['id']
    obj = MaterialQuality.objects.get(id=id)
    obj.delete()
    return JsonResponse({'status':1})
