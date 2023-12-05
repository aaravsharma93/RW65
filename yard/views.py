from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from .render import Render
from .forms import *
from datetime import datetime
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import re
from django.utils.translation import get_language
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from .models import User, ForeignWeigh
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
import json
import socket
# import pandas as pd
from django.contrib import messages
from .utils import get_image_data
from .utils.view_handling import set_settings_session, yard_check, user_role, save_base64, set_cxt, set_ss_cxt

Yard_User = get_user_model()
the_socket = None


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def home(request):
    if request.user.role == "selfservice":
        return redirect("ss_home")

    F = ForeignFlag.objects.all().last()
    if F is not None:
        if F.status == 1:
            obj = Transaction.objects.get(id=request.session['transaction_id'])
            foreign = ForeignWeigh(customer=obj.customer, supplier=obj.supplier, article=obj.article,
                                   vehicle=obj.vehicle,
                                   first_weight=obj.first_weight, second_weight=obj.second_weight,
                                   net_weight=obj.net_weight,
                                   total_price=obj.total_price, status=obj.status,
                                   updated_date_time=obj.updated_date_time,
                                   secondw_alibi_nr=obj.secondw_alibi_nr, transaction_id=obj.id)
            foreign.save()
            if obj.customer is not None:
                customer = get_object_or_404(Customer, id=obj.customer.id)
                customer.delete()
            if obj.supplier is not None:
                supplier = get_object_or_404(Supplier, id=obj.supplier.id)
                supplier.delete()
            if obj.article is not None:
                article = get_object_or_404(Article, id=obj.article.id)
                article.delete()
            if obj.vehicle is not None:
                vehicle = get_object_or_404(Vehicle, id=obj.vehicle.id)
                vehicle.delete()
            if obj.container is not None:
                container = get_object_or_404(Container, id=obj.container.id)
                container.delete()
            obj.delete()
            ForeignFlag.objects.all().delete()
    print(get_language())
    form = CombinationForm(request.POST or None)
    # if request.POST.get('foreignn') == '1':
    if request.POST:
        if 'save_button' in request.POST:
            id = request.POST.get('id')
            trans_flag = request.POST.get('trans_flag')
            if trans_flag:
                con = transaction_save(request)
            else:
                messages.error(request, "Wiegen Nicht durchgeführt ")
            try:
                obj = Combination.objects.get(id=id)
            except:
                obj = None
            if obj == None:
                if form.is_valid():
                    comp_obj = form.instance
                    comp_obj.yard = request.user.yard
                    comp_obj.transaction_id = con['dataset'].id
                    comp_obj.save()
                    form.save()
                    CombinationForm(None)

                    return HttpResponseRedirect("/")

            form = CombinationForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # obj = form.instance
                # obj.transaction_id = con['dataset'].id
                # obj.save()
                CombinationForm(None)

            context = set_cxt(request)
            context["off"] = True
            return render(request, "yard/index2.html", context)
        elif 'print_button' in request.POST:
            context_transaction = transaction_save(request)
            return Render.render("yard/pdf_template.html", context_transaction)
        elif 'save_comb' in request.POST:
            context_save = transaction_save(request)
            id = request.POST.get('id')
            try:
                obj = Combination.objects.get(id=id)
            except:
                obj = None
            if obj == None:
                if form.is_valid():
                    comp_obj = form.instance
                    comp_obj.yard = request.user.yard
                    comp_obj.save()
                    form.save()
                    CombinationForm(None)
                    messages.success(request, "ID gespeichert")
                    return HttpResponseRedirect("/")

            form = CombinationForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                CombinationForm(None)
                messages.success(request, "ID aktualisiert")
            context = set_cxt(request)
            context["off"] = True
            return render(request, "yard/index2.html", context)
        else:
            context = set_cxt(request)
            context["off"] = True
            return render(request, "yard/index2.html", context)
    context = set_cxt(request)
    context["off"] = True
    return render(request, "yard/index2.html", context)


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def self_service_home(request):
    
    form = CombinationForm(request.POST or None)
    # if request.POST.get('foreignn') == '1':
    if request.POST:
        if 'save_button' in request.POST:
            id = request.POST.get('id')
            trans_flag = request.POST.get('trans_flag')
            if trans_flag:
                transaction_save(request)
            else:
                messages.error(request, "Wiegen Nicht durchgeführt ")
            try:
                obj = Combination.objects.get(id=id)
            except:
                obj = None
            if obj == None:
                if form.is_valid():
                    comp_obj = form.instance
                    comp_obj.yard = request.user.yard
                    comp_obj.save()
                    form.save()
                    CombinationForm(None)

                    return HttpResponseRedirect("/")

            form = CombinationForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                CombinationForm(None)

            context = set_ss_cxt(request)
            return render(request, "yard/self_service_home.html", context)
        elif 'print_button' in request.POST:
            context_transaction = transaction_save(request)
            return Render.render("yard/pdf_template.html", context_transaction)
        else:
            context = set_ss_cxt(request)
            return render(request,  "yard/self_service_home.html", context)
    context = set_ss_cxt(request)
    return render(request,  "yard/self_service_home.html", context)


"""  Sign up form which will be visible to only superuser """
""" Sign in form view """


@user_passes_test(lambda u: not u.is_authenticated, redirect_field_name=None, login_url='/sign_out')
def sign_in(request):
    context = {}
    form = CustomLoginForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(username=email, password=password)
            if user is not None:
                yard_id = Yard_list.objects.first()
                if yard_id is not None:
                    login(request, user)
                    if user.yard == None:
                        user.yard = yard_id
                        user.save()
                    if user.role == "selfservice":
                        return redirect("ss_home")
                    return redirect('home')
                else:
                    request.session['email'] = email
                    request.session['password'] = password
                    return redirect('yard_creation')
            else:
                context['error'] = "Invalid Credentials or Login"
    context['form'] = form
    return render(request, 'registration/login2.html', context)


""" sign out view """


@login_required()
def sign_out(request):
    logout(request)
    return redirect('/sign_in/')


""" all registered yard users list view  and update user view"""


@user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def users_list(request):
    context = {}
    if request.POST:
        id_ = request.POST.get('id')
        password = request.POST.get('password1')
        role = request.POST.get('role')
        if role is None:
            role = 'operator' if request.user.is_superuser == False else 'superuser'
        address = request.POST.get('address')
        telephone = request.POST.get('telephone')
        form = SignUpForm(request.POST or None)
        obj = get_object_or_404(Yard_User, id=id_) if id_ else None
        if obj:
            form = UserUpdateForm(
                request.POST, instance=obj) if password == obj.password else form
            address = request.user.address if id_ == request.user.id else address
            telephone = request.user.telephone if id_ == request.user.id else telephone

        if form.is_valid():
            user = form.save(commit=False)
            user.role = role
            user.address = address
            user.telephone = telephone
            user.is_superuser = user.is_staff = True if role == 'superuser' else False
            user.save()
            return redirect('users_list')
    form = SignUpForm(request.POST or None)
    context['form'] = form
    context["dataset"] = Yard_User.objects.all()
    return render(request, 'registration/userlist.html', context)


""" return data for specific user """


def user_edit(request):
    context = {}
    if request.POST:
        id_ = request.user.id
        role = request.user.role
        if role == '':
            role = 'operator' if request.user.is_superuser == False else 'superuser'
        yard = request.user.yard
        obj = get_object_or_404(Yard_User, id=id_) if id_ else None
        form = UserUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = role
            user.yard = yard
            user.is_superuser = user.is_staff = True if role == 'superuser' or role == 'technician' else False
            user.save()
            return redirect('user_edit')
    form = UserUpdateForm(request.POST or None)
    context['form'] = form
    context["dataset"] = Yard_User.objects.get(id=request.user.id)
    return render(request, 'registration/user_edit.html', context)


# @user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def users_details(request, identifier):
    obj = get_object_or_404(Yard_User, id=identifier)
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


""" delete user view """


@user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def user_delete(request, identifier):
    obj = get_object_or_404(Yard_User, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/users_list")


# Self Service User Views

# @user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def get_ss_user(request):
    context = {}
    ss_users = User.objects.filter(role="selfservice")
    context["ss_users"] = ss_users
    return render(request, "yard/SelfService.html", context)
    # return JsonResponse(json.loads(serialize('json', ss_users)), safe=False)


# @user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def get_auth_ss_fields(request, id):
    try:
        user = User.objects.get(id=id)
        ss_articles = json.loads(serialize('json', user.article_set.all()))
        ss_customers = json.loads(serialize('json', user.customer_set.all()))
        ss_sites = json.loads(serialize('json', user.buildingsite_set.all()))
        ss_vehicles = json.loads(serialize('json', user.vehicle_set.all()))
        ss_suppliers = json.loads(serialize('json', user.supplier_set.all()))
        ss_containers = json.loads(serialize('json', user.container_set.all()))
        response = {
            "articles": ss_articles,
            "customers": ss_customers,
            "building_sites": ss_sites,
            "vehicles": ss_vehicles,
            "suppliers": ss_suppliers,
            "containers": ss_containers
        }

        return JsonResponse(response)

    except User.DoesNotExist as e:
        return JsonResponse({"status": "User does not exist"})


# @user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
def get_field_values(request):
    articles = json.loads(serialize("json", Article.objects.all()))
    customers = json.loads(serialize("json", Customer.objects.all()))
    building_sites = json.loads(serialize("json", BuildingSite.objects.all()))
    vehicles = json.loads(serialize("json", Vehicle.objects.all()))
    suppliers = json.loads(serialize("json", Supplier.objects.all()))
    containers = json.loads(serialize("json", Container.objects.all()))
    response = {
        "articles": articles,
        "customers": customers,
        "building_sites": building_sites,
        "vehicles": vehicles,
        "suppliers": suppliers,
        "containers": containers
    }
    return JsonResponse(response)


# @user_passes_test(lambda u: u.is_superuser, redirect_field_name=None)
@csrf_exempt
def update_ss_field(request):
    fields = {
        "articles": Article,
        "customers": Customer,
        "building_sites": BuildingSite,
        "vehicles": Vehicle,
        "suppliers": Supplier,
        "containers": Container
    }

    if request.method == "PUT":
        form = SSUpdateForm(data=json.loads(request.body))
        if form.is_valid():
            field_values = form.cleaned_data["values"]
            user = User.objects.get(id=form.cleaned_data["user"])

            ThroughModel = fields[form.cleaned_data["field_type"]
                                  ].ss_role_access.through
            field_user = ThroughModel.objects.filter(user_id=user.id)
            field_user.delete()

            if len(field_values) > 0:
                # field_objs = Article.objects.filter(id__in=field_values)
                field_value_objs = fields[form.cleaned_data["field_type"]].objects.filter(
                    id__in=field_values)
                field_user_objs = []
                for value in field_value_objs:
                    param_dict = {
                        "user_id": user.id,
                        fields[form.cleaned_data["field_type"]].__name__.lower(): value
                    }
                    field_user_objs.append(ThroughModel(**param_dict))
                ThroughModel.objects.bulk_create(field_user_objs)
            response = json.loads(
                serialize("json", fields[form.cleaned_data["field_type"]].objects.filter(ss_role_access__in=[user, ])))
            return JsonResponse(response, safe=False)

        else:
            return JsonResponse({"status": form.errors}, status=400)


# function for saving Transaction, also saves respected data if not existing
def transaction_save(request):
    context = {}
    # import pdb; pdb.set_trace()
    absolute_url = request.build_absolute_uri('?')
    context["absolute_url"] = "http://" + request.get_host()
    context['logo'] = Logo.objects.all()
    context['role'] = request.user.role
    context['user_name'] = request.user.name
    context['sign'] = Signature.objects.filter(user=request.user).last()
    context['customer'] = request.session['customer'] if request.session['customer'] else 'Kunde'
    context['article'] = request.session['article'] if request.session['article'] else 'Artikel'
    context['show_price'] = request.POST.get('show_price')
    context['show_container'] = request.POST.get('contr_on')
    context['showt'] = ShowTonne.objects.all().last()
    context['io'] = Io.objects.all().last()
    context['tara_date'] = request.POST.get('tara_date')
    # print(context)
    form = TransactionForm(request.POST or None)
    # print(form.data)
    vehicle_id = form["vehicle"].data
    customer_id = form["customer"].data
    container_id = form["container"].data
    # container_id = request.POST.get('id_container')
    article_id = form["article"].data
    supplier_id = form["supplier"].data
    first_weight = form["first_weight"].data
    second_weight = form["second_weight"].data
    net_weight = form["net_weight"].data
    firstw_date_time = form["firstw_date_time"].data
    secondw_date_time = form["secondw_date_time"].data
    firstw_alibi_nr = form["firstw_alibi_nr"].data
    secondw_alibi_nr = form["secondw_alibi_nr"].data
    print(first_weight)
    foreign = request.POST.get('foreign')
    trans_flag = request.POST.get('trans_flag')

    if request.POST:
        # edit or update Customer details
        if customer_id:
            try:
                if re.match('^[0-9]*$', customer_id):
                    customer = Customer.objects.get(id=customer_id)
                else:
                    customer = Customer.objects.get(name1=customer_id)
            except:
                customer = Customer.objects.create(name1=customer_id)
            customer.price_group = request.POST.get("customer_price_group")
            customer.street = request.POST.get("customer_street")
            customer.name2 = request.POST.get("customer_name2")
            customer.pin = request.POST.get("customer_pin")
            customer.place = request.POST.get("customer_place")
            customer.save()
            request.POST._mutable = True
            request.POST["customer"] = customer.id

        # edit or update article details
        if article_id:
            firstweight = form["first_weight"].data
            print('bbbbbbbbbbbbbbb')
            print(firstweight)
            secondweight = form["second_weight"].data
            try:
                if re.match('^[0-9]*$', article_id):
                    article = Article.objects.get(id=article_id)
                else:
                    article = Article.objects.get(
                        name=article_id, yard=request.user.yard)
            except:
                item_price = request.POST.get('price_per_item') if request.POST.get(
                    'price_per_item') != '' else 0
                # item_price = Decimal(request.POST.get('price_per_item'))
                article = Article.objects.create(name=article_id, price1=item_price, price2=item_price,
                                                 price3=item_price,
                                                 price4=item_price, price5=item_price, yard=request.user.yard)
            # article.short_name= request.POST.get("article_short_name")
            article.group = request.POST.get("article_group")
            article.yard = request.user.yard
            if request.POST.get('article_vat') is not None and request.POST.get('article_vat') != '':
                article.vat = float(request.POST.get('article_vat'))
            if float(firstweight) > float(secondweight):
                print("if ", firstweight, secondweight)
                article.balance_weight = Decimal(article.entry_weight) + abs(
                    Decimal(firstweight) - Decimal(secondweight))
                article.entry_weight = Decimal(article.balance_weight) + abs(
                    Decimal(firstweight) - Decimal(secondweight))
            else:
                print("else", firstweight, secondweight)
                w1 = Decimal(article.balance_weight) - \
                    abs(Decimal(secondweight) - Decimal(firstweight))
                article.balance_weight = w1 if w1 > 0 else 0.0
                article.outgoing_weight = Decimal(article.outgoing_weight) + abs(
                    Decimal(secondweight) - Decimal(firstweight))
            article.save()
            request.POST._mutable = True
            request.POST["article"] = article.id

        # edit or update lieferanten details
        if supplier_id:
            try:
                if re.match('^[0-9]*$', supplier_id):
                    supplier = Supplier.objects.get(id=supplier_id)
                else:
                    supplier = Supplier.objects.get(supplier_name=supplier_id)
            except:
                supplier = Supplier.objects.create(supplier_name=supplier_id)
            # supplier.short_name = request.POST.get("supplier_short_name")
            supplier.street = request.POST.get("supplier_street")
            supplier.pin = request.POST.get("supplier_pin")
            supplier.first_name = request.POST.get("supplier_firstname")
            supplier.place = request.POST.get("supplier_place")
            supplier.save()
            request.POST._mutable = True
            request.POST["supplier"] = supplier.id

        # edit or update Fahrzeuge details
        if vehicle_id:
            try:
                if re.match('^[0-9]*$', vehicle_id):
                    vehicle = Vehicle.objects.get(id=vehicle_id)
                else:
                    vehicle = Vehicle.objects.get(license_plate=vehicle_id)
            except:
                vehicle = Vehicle.objects.create(license_plate=vehicle_id)
            try:
                vehicle.forwarder = Forwarders.objects.get(
                    id=request.POST.get("vehicle_forwarder"))
            except:
                pass
            vehicle.vehicle_weight = request.POST.get("vehicle_weight")
            if vehicle.vehicle_weight == '':
                vehicle.vehicle_weight = 0
            vehicle.license_plate2 = request.POST.get("license_plate2")
            vehicle.save()
            request.POST._mutable = True
            request.POST["vehicle"] = vehicle.id

        # if container_id != '0' and container_id != None:
        if container_id:
            try:
                if re.match('^[0-9]*$', container_id):
                    container = Container.objects.get(id=container_id)
                else:
                    container = Container.objects.get(name=container_id)
            except:
                container = Container.objects.create(name=container_id)

            container.container_type = request.POST.get("contr_type")
            container.container_group = request.POST.get("contr_group")
            container.container_weight = request.POST.get("contr_weight", 0)
            container.save()
            request.POST._mutable = True
            request.POST["container"] = container.id
        trans_id = request.POST.get('trans_id')

        ### FOR EXTERNAL WEIGHING ###
        if foreign == '1':
            if trans_flag == '1':
                request.session['transaction_id'] = trans_id
                F = ForeignFlag(status=1)
                F.save()
        ##############################

        try:
            obj = Transaction.objects.get(id=trans_id)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                trans_obj = form.instance
                if request.POST.get('id') != '0':
                    trans_obj.combination_id = request.POST.get('id')
                trans_obj.yard = request.user.yard
                status = request.POST.get('status')
                if status is not None:
                    trans_obj.status = status
                if 'save_button' in request.POST:
                    messages.success(
                        request, "Wiegung erfolgreich durchgeführt.")

                item_price = request.POST.get('price_per_item')
                if item_price is not None:
                    net_weight = int(request.POST.get('net_weight')) / 100
                    if item_price == '':
                        item_price = 1
                    price_total = float(net_weight) * float(item_price)
                    trans_obj.total_price = price_total
                    if request.POST.get('article_vat') is not None and request.POST.get('article_vat') != '':
                        print(request.POST.get('article_vat'))
                        context['tax'] = (
                            price_total * float(request.POST.get('article_vat'))) / 100
                        context['price_after_tax'] = (
                            price_total * float(request.POST.get('article_vat'))) / 100 + price_total
                trans_obj.save()
                item_saved = form.save()

                save_base64(request, item_saved.pk)
                try:
                    obj = Transaction.objects.get(id=item_saved.pk)
                except:
                    obj = None
                context["dataset"] = obj
                context["images"] = obj.images_base64_set.first()
                return context
            else:
                print("error", form.errors)
        form = TransactionForm(request.POST, instance=obj)
        if form.is_valid():
            t_obj = form.instance
            if request.POST.get('id') != '0':
                t_obj.combination_id = request.POST.get('id')
            status = request.POST.get('status')
            if status is not None:
                t_obj.status = status
            item_price = request.POST.get('price_per_item')
            if item_price is not None:
                net_weight = int(request.POST.get('net_weight')) / 100
                if item_price == '':
                    item_price = 1
                price_total = float(net_weight) * float(item_price)
                t_obj.total_price = price_total
                if request.POST.get('article_vat') is not None and request.POST.get('article_vat') != '':
                    context['price_after_tax'] = (
                        price_total * float(request.POST.get('article_vat'))) / 100 + price_total
            t_obj.save()
            obj = form.save()
            save_base64(request, obj.id)
            context["dataset"] = obj
            context["images"] = obj.images_base64_set.first() if obj else None
        else:
            print("error", form.errors)

    return context


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def yard_list(request):
    context = {}
    form = yardListForm(request.POST or None)

    if request.POST:
        idd = request.POST.get('id')
        try:
            obj = Yard_list.objects.get(id=idd)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = yardListForm(None)
            context['form'] = form
            context["dataset"] = Yard_list.objects.all()
            return render(request, "yard/yard_list2.html", context)
        # to handle update TBD
        form = yardListForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = yardListForm(None)
        context["form"] = form
        context["dataset"] = Yard_list.objects.all()
        return render(request, "yard/yard_list2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Yard_list.objects.all()
        return render(request, "yard/yard_list2.html", context)


# API for loading details from ajax to editform
@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def yard_list_detail(request, identifier):
    try:
        obj = Yard_list.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def yard_list_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Yard_list, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/yard_list")


def yard_creation(request):
    context = {}
    form = yardListForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            yard_saved = form.save()
            yardListForm(None)
            email = request.session['email']
            password = request.session['password']
            user = authenticate(username=email, password=password)
            login(request, user)
            user.yard = yard_saved
            user.save()
            try:
                del request.session['email']
                del request.session['password']
            except:
                pass
        return render(request, "yard/index2.html", context)
    else:
        if request.session.get('email') is not None:
            context["form"] = form
            return render(request, "yard/yard_creation.html", context)
        else:
            return redirect('sign_in')


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def article(request):
    context = {}
    form = ArticleForm(request.POST or None)

    if request.POST:
        id = request.POST.get('id')
        new_quantity = request.POST.get('update_quantity')
        try:
            obj = Article.objects.get(id=id)
            incoming_quantity = float(obj.entry_weight) + float(new_quantity)
            remaining_quantity = float(
                obj.balance_weight) + float(new_quantity)
        except:
            obj = None
            incoming_quantity = new_quantity
            remaining_quantity = new_quantity
        if obj == None:
            if form.is_valid():
                art_obj = form.instance
                art_obj.yard = request.user.yard
                art_obj.entry_weight = float(incoming_quantity) if float(
                    incoming_quantity) > 0 else 0.0
                art_obj.balance_weight = float(remaining_quantity) if float(
                    remaining_quantity) > 0 else 0.0
                art_obj.save()
                form.save()
                form = ArticleForm(None)
            context['form'] = form
            context["dataset"] = Article.objects.filter(yard=request.user.yard)
            # context["art_meta"] = Article_meta.objects.all()
            return render(request, "yard/article2.html", context)
        # to handle update TBD
        form = ArticleForm(request.POST, instance=obj)
        if form.is_valid():
            art_obj = form.instance
            # art_obj.yard = request.user.yard
            art_obj.entry_weight = float(incoming_quantity) if float(
                incoming_quantity) > 0 else 0.0
            art_obj.balance_weight = float(remaining_quantity) if float(
                remaining_quantity) > 0 else 0.0
            art_obj.save()
            form.save()
            form = ArticleForm(None)
        context["form"] = form
        context["dataset"] = Article.objects.filter(yard=request.user.yard)
        return render(request, "yard/article2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Article.objects.filter(yard=request.user.yard)
        return render(request, "yard/article2.html", context)


@login_required
def article_detail(request, identifier):
    try:
        obj = Article.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
        if obj.ware_house:
            ware = model_to_dict(obj.ware_house)
        else:
            ware = {}
        del data["ss_role_access"]
    else:
        data = {}
        ware = {}
    return JsonResponse({'data': data, 'ware_house': ware})


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def article_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Article, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/article")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def article_list(request):
    # if request.is_ajax():
    # queryset = json.loads(serialize('json', Article.objects.all()))
    queryset = json.loads(
        serialize('json', Article.objects.filter(yard=request.user.yard)))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


@login_required
@user_passes_test(yard_check)
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def building_site(request):
    context = {}
    form = BuildingSiteForm(request.POST or None)

    if request.POST:
        id = request.POST.get('id')
        try:
            obj = BuildingSite.objects.get(id=id)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = BuildingSiteForm(None)
            context['form'] = form
            context["dataset"] = BuildingSite.objects.all()
            return render(request, "yard/building_site2.html", context)
        # to handle update TBD
        form = BuildingSiteForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = BuildingSiteForm(None)
        context["form"] = form
        context["dataset"] = BuildingSite.objects.all()
        return render(request, "yard/building_site2.html", context)
    else:
        context["form"] = form
        context["dataset"] = BuildingSite.objects.all()
        return render(request, "yard/building_site2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def building_site_detail(request, identifier):
    try:
        obj = BuildingSite.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def building_site_delete(request, identifier):
    context = {}
    obj = get_object_or_404(BuildingSite, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/building_site")


@login_required
@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def delivery_note(request):
    context = {}
    form = Delivery_noteForm(request.POST or None)

    if request.POST:
        id = request.POST.get('id')
        print("Id: " + id)
        try:
            obj = Delivery_note.objects.get(id=id)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = Delivery_noteForm(None)
            context['form'] = form
            context["dataset"] = Delivery_note.objects.all()
            return render(request, "yard/delivery_note2.html", context)
        # to handle update TBD
        form = Delivery_noteForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = Delivery_noteForm(None)
        context["form"] = form
        context["dataset"] = Delivery_note.objects.all()
        return render(request, "yard/delivery_note2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Delivery_note.objects.all()
        return render(request, "yard/delivery_note2.html", context)


# API for loading details from ajax to editform
@login_required(redirect_field_name=None)
def delivery_note_detail(request, identifier):
    try:
        obj = Delivery_note.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
@login_required(redirect_field_name=None)
def delivery_note_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Delivery_note, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/delivery_note")


@login_required(redirect_field_name=None)
@user_passes_test(yard_check)
def pdf_template(request):
    context = {
        "lfd_nr": "123",
        "file_name": "Sample File",
        "note_date": "12-12-2020",
    }
    return Render.render("yard/pdf_template.html", context)


def customer_popup(request):
    context = {}
    # form = CustomerSearchForm(request.POST or None)
    if request.POST:
        pass
    # idd=request.POST.get('search_key')
    # context["form"] = form
    context["dataset"] = Customer.objects.all()
    return render(request, "yard/customer_popup.html", context)


def material_popup(request):
    context = {}
    # form = CustomerSearchForm(request.POST or None)
    if request.POST:
        pass
    # idd=request.POST.get('search_key')
    # context["form"] = form
    context["dataset"] = Article.objects.all()
    return render(request, "yard/material_popup.html", context)


def vehicle_popup(request):
    context = {}
    # form = CustomerSearchForm(request.POST or None)
    if request.POST:
        pass
    # idd=request.POST.get('search_key')
    # context["form"] = form
    context["dataset"] = Vehicle.objects.all()
    return render(request, "yard/vehicle_popup.html", context)


def supplier_popup(request):
    context = {}
    # form = CustomerSearchForm(request.POST or None)
    if request.POST:
        pass
    # idd=request.POST.get('search_key')
    # context["form"] = form
    context["dataset"] = Supplier.objects.all()
    return render(request, "yard/supplier_popup.html", context)


def transcation_popup(request):
    context = {}
    context["dataset"] = Transaction.objects.filter(
        trans_flag=0, yard=request.user.yard)
    return render(request, "yard/transcation_popup.html", context)


# API for loading details from ajax
def transcation_detail(request, identifier):
    try:
        obj = Transaction.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
        img_data = obj.images_base64_set.first()
        if (img_data):
            images = {
                "image1": get_image_data(
                    "http://" + request.get_host() + img_data.image1.url) if img_data.image1 else None,
                "image2": get_image_data(
                    "http://" + request.get_host() + img_data.image2.url) if img_data.image2 else None,
                "image3": get_image_data(
                    "http://" + request.get_host() + img_data.image3.url) if img_data.image3 else None
            }
            data["images"] = images
        else:
            images = {
                "image1": None,
                "image2": None,
                "image3": None
            }
            data["images"] = images
    else:
        data = {}
    return JsonResponse(data)


# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
@login_required
@user_passes_test(yard_check)
def container(request):
    context = {}
    form = ContainerForm(request.POST or None)

    if request.POST:
        idd = request.POST.get('id')
        try:
            obj = Container.objects.get(id=idd)
        except:
            obj = None
        if obj == None:
            if form.is_valid():
                form.save()
                form = ContainerForm(None)
            context['form'] = form
            context["dataset"] = Container.objects.all()
            return render(request, "yard/container2.html", context)
        # to handle update TBD
        form = ContainerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            form = ContainerForm(None)
        context["form"] = form
        context["dataset"] = Container.objects.all()
        return render(request, "yard/container2.html", context)
    else:
        context["form"] = form
        context["dataset"] = Container.objects.all()
        return render(request, "yard/container2.html", context)


# API for loading details from ajax to editform
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def container_details(request, identifier):
    try:
        obj = Container.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
    else:
        data = {}
    return JsonResponse(data)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def container_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Container, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/container")


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def container_list(request):
    # if request.is_ajax():
    queryset = json.loads(serialize('json', Container.objects.all()))
    list = []
    data = {
        'list': queryset,
    }
    return JsonResponse(data)


# @login_required
def scale_data(request):
    # HOST = '109.90.104.232'
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 3200
    try:
        cmd = request.GET["cmd"]
    except MultiValueDictKeyError as e:
        cmd = "GET WEIGHT"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(cmd.encode("UTF-8"))
        data = ""
        while True:
            part = s.recv(1024)
            if len(part) == 0:
                break
            else:
                data += part.decode("UTF-8")
        return JsonResponse(json.loads(data))
