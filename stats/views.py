import io
import shlex
import shutil
import subprocess
import xml.etree.cElementTree as ET
import re

import zipfile
from io import StringIO
from django.core import management
from django.contrib import messages
from django.shortcuts import redirect
import xlwt
from email.encoders import encode_base64
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings
from django.core.files.storage import default_storage
from django.db.models import Q, Sum, When, Exists
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from yard.render import Render

from yard.models import *
from yard.forms import *
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json
from datetime import datetime, date, timedelta
from yard.utils.field_statistics import field_func
from yard.utils.smtp_ops import send_mail
from yard.utils.view_handling import create_excel
from django.http import FileResponse, Http404
import os
import sqlite3
import datetime
from datetime import datetime
from django.db import connection

LOGO_DIR = "/var/www/html/pdfdemo"
PDF_DIR = "/var/www/html/pdfdemo"
PDF_BASE_NAME = "delivery_note"
PDF_LATEX = "pdflatex"


@login_required(redirect_field_name=None)
def std_evaluation1(request):
    context = {}
    absolute_url = request.build_absolute_uri('?')
    context["absolute_url"] = "http://" + request.get_host()

    if request.POST:
        note_type = request.POST.getlist('note_type')
        grouping = request.POST.get('grouping')
        fromdate = request.POST.get('fromdate')

        if fromdate:
            context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
            fromdate = fromdate + " 00:00:00"
        else:
            fromdate = str(date.today()) + " 00:00:00"

        todate = request.POST.get('todate')
        if todate:
            context['to'] = datetime.strptime(todate, "%Y-%m-%d")
            todate = todate + " 23:59:59"
        else:
            todate = str(date.today()) + " 23:59:59"

        article_from = request.POST.get('article_from')
        article_to = request.POST.get('article_to')
        print("Grouping:", grouping)
        obj = Transaction.objects.filter(created_date_time__range=(fromdate, todate))
        # obj = Transkation.objects.raw('SELECT *,SUM(net_weight) as ttl FROM yard_transkation WHERE created_date_time BETWEEN %s and %s GROUP BY(article_id)',[fromdate,todate])
        sum_kg = 0
        if obj:
            if grouping == 'article':
                # context["data"] = get_article_groupset(obj)
                context['date'] = datetime.now()
                context["data"] = obj
                context["art_list"] = obj.values_list("article", "article__description").distinct()
                art_sum = []
                context["art_list"] = [list(i) for i in context["art_list"]]
                for i in context["art_list"]:
                    i.append(sum(j.net_weight for j in obj if j.article.pk == i[0]))
                context["art_sum"] = art_sum
                return Render.render("stats/pdf/article_report.html", context)
            elif grouping == 'art-cus':
                print("article customer")
                context["data"] = obj
                context['date'] = datetime.now()
                context["art_list"] = obj.values_list("article", "article__description").distinct()
                context["cus_list"] = obj.values_list("customer", "customer__name").distinct()
                art_sum = []
                context["art_list"] = [list(i) for i in context["art_list"]]
                context["cus_list"] = [list(i) for i in context["cus_list"]]
                context["summ"] = []
                for i in context["art_list"]:
                    for k in context["cus_list"]:
                        temp = {}
                        for j in obj:
                            summ = 0
                            temp["article"] = i[0]
                            temp["customer"] = k[0]
                            # if j.article.pk==i[0] and j.customer.pk==k[0]:
                            # summ=summ+j.net_weight
                            temp["sum"] = sum(
                                j.net_weight for j in obj if j.article.pk == i[0] and j.customer.pk == k[0])
                        context["summ"].append(temp)
                return Render.render("stats/pdf/art_cus_report.html", context)
            elif grouping == 'cus-art':
                print("customer article")
                context["data"] = obj
                context['date'] = datetime.now()
                context["art_list"] = obj.values_list("article", "article__description").distinct()
                context["cus_list"] = obj.values_list("customer", "customer__name").distinct()
                context["art_list"] = [list(i) for i in context["art_list"]]
                context["cus_list"] = [list(i) for i in context["cus_list"]]
                context["summ"] = []
                for i in context["cus_list"]:
                    for k in context["art_list"]:
                        temp = {}
                        for j in obj:
                            summ = 0
                            temp["article"] = k[0]
                            temp["customer"] = i[0]
                            # if j.article.pk==i[0] and j.customer.pk==k[0]:
                            # summ=summ+j.net_weight
                            temp["sum"] = sum(
                                j.net_weight for j in obj if j.article.pk == k[0] and j.customer.pk == i[0])
                        context["summ"].append(temp)
                    # context["sum"].append(sum(j.net_weight for j in obj if j.article.pk==i[0] and j.customer.pk==k[0]))
                return Render.render("stats/pdf/cus_art_report.html", context)
                context["data"] = obj
        else:
            context['error'] = "No Transkations found!"
            return render(request, "stats/std_evaluation2.html", context)
    return render(request, "stats/std_evaluation2.html", context)


@login_required(redirect_field_name=None)
def daily_delivery_list(request):
    context = {}
    form = TransactionForm(request.POST or None)

    if request.POST:
        if 'print_button' in request.POST:
            context_transaction = transaction_update(request)
            return Render.render("yard/pdf_template.html", context_transaction)
        elif 'save_button' in request.POST:
            id = request.POST.get('id')
            obj = Transaction.objects.get(id=id)
            form = TransactionForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            else:
                print("error", form.errors)
    fromdate = request.POST.get('fromdate')
    if fromdate is not None:
        fromdate = fromdate + " 00:00:00.000000"
    else:
        fromdate = str(date.today()) + " 00:00:00"
    todate = request.POST.get('todate')
    if todate is not None:
        todate = todate + " 23:59:59.000000"
    else:
        todate = str(date.today()) + " 23:59:59"
    context["form"] = form
    context['daily'] = True
    context["dataset"] = Transaction.objects.filter(updated_date_time__range=(fromdate, todate), trans_flag=1,
                                                    yard=request.user.yard)
    return render(request, "stats/deliverynotes2.html", context)


@login_required(redirect_field_name=None)
def send_delivery_note(request, trans_id):
    try:
        trans_obj = Transaction.objects.get(id=trans_id)
        cust_obj = trans_obj.customer
        settings = Settings.objects.first()
        if settings is None:
            return JsonResponse({"status": "Settings Not Found"}, status=404)
        if not settings.smtp_support:
            return JsonResponse({"status": "SMTP Credentials Not Found"}, status=404)
        smtp_obj = settings.smtp_creds
        if cust_obj is None:
            return JsonResponse({"status": "Customer Not Found"}, status=404)
        else:
            if cust_obj.contact_person1_email:
                message_text = f'Your Delivery Note With Code {trans_obj.id}'
                pdf = Render.static_render("yard/pdf_template.html",
                                           trans_obj.get_context_transaction(request)).getvalue()
                message = MIMEMultipart()
                message['From'] = smtp_obj.sender_address
                message['To'] = cust_obj.contact_person1_email
                message.attach(MIMEText(message_text, 'plain'))
                pdf_attach = MIMEApplication(pdf, _subtype="pdf", _encoder=encode_base64)
                pdf_attach.add_header('content-disposition', 'attachment', filename="ExamplePDF.pdf")
                message.attach(pdf_attach)
                send_mail(smtp_obj, message.as_string(), {cust_obj.contact_person1_email, })
                return JsonResponse({"status": "Email Sent"})
            else:
                return JsonResponse({"status": "Customer Does not have email"}, status=404)
    except Transaction.DoesNotExist as e:
        return JsonResponse({"status": "Transaction Not Found"}, status=404)


@login_required(redirect_field_name=None)
def deliverynotes(request):
    context = {}
    form = TransactionForm(request.POST or None)
    if request.POST:
        if 'print_button' in request.POST:
            context_transaction = transaction_update(request)
            return Render.render("yard/pdf_template.html", context_transaction)

        elif 'date_selection' in request.POST:
            fromdate = request.POST.get('fromdate')
            if fromdate:
                context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
                fromdate = fromdate + " 00:00:00"
            else:
                fromdate = str(date.today() - timedelta(days=7)) + " 00:00:00"

            todate = request.POST.get('todate')
            if todate:
                context['to'] = datetime.strptime(todate, "%Y-%m-%d")
                todate = todate + " 23:59:59"
            else:
                todate = str(date.today()) + " 23:59:59"

            context["form"] = form
            context["dataset"] = Transaction.objects.filter(updated_date_time__range=(fromdate, todate), trans_flag=1,
                                                            yard=request.user.yard).order_by('-updated_date_time')
            return render(request, "stats/deliverynotes2.html", context)
        elif 'mail_data' in request.POST:
            fromdate = request.POST.get('fromdate')
            if fromdate:
                context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
                fromdate = fromdate + " 00:00:00"
            else:
                fromdate = str(date.today() - timedelta(days=7)) + " 00:00:00"

            todate = request.POST.get('todate')
            if todate:
                context['to'] = datetime.strptime(todate, "%Y-%m-%d")
                todate = todate + " 23:59:59"
            else:
                todate = str(date.today()) + " 23:59:59"

            Data = Transaction.objects.filter(updated_date_time__range=(fromdate, todate), trans_flag=1,
                                              yard=request.user.yard)

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Lieferschein.xls"'
            wb = create_excel(Data)
            wb.save(response)
            settings = Settings.objects.first()
            smtp_obj = settings.smtp_creds
            message = MIMEMultipart()
            if smtp_obj is not None:
                message['From'] = smtp_obj.sender_address
                message['To'] = settings.company_email
                message['Subject'] = f"Report For Delivery Notes between {fromdate} and {todate}"
                att = MIMEText(response.content, 'base64', 'utf-8')
                att["Content-Type"] = 'application/ms-excel'
                att['Content-Disposition'] = 'attachment; filename ="%s"' % "test.xls"
                message.attach(att)
                send_mail(smtp_obj, message.as_string(), {settings.company_email, })
                return response
            else:
                messages.error(request, "Bitte richten Sie E-Mail in den Einstellungen ein")
                # return HttpResponseRedirect('/stats/deliverynotes')

        elif 'export_data' in request.POST:
            fromdate = request.POST.get('fromdate')
            if fromdate:
                fromdate = fromdate + " 00:00:00"
            else:
                fromdate = str(date.today() - timedelta(days=7)) + " 00:00:00"

            todate = request.POST.get('todate')
            if todate:
                todate = todate + " 23:59:59"
            else:
                todate = str(date.today()) + " 23:59:59"

            Data = Transaction.objects.filter(updated_date_time__range=(fromdate, todate),
                                              yard=request.user.yard)

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Lieferschein.xls"'
            wb = create_excel(Data)
            wb.save(response)
            return response

        else:
            id = request.POST.get('id')
            if id:
                obj = Transaction.objects.get(id=id)
                form = TransactionForm(request.POST, instance=obj)
                if form.is_valid():
                    form.save()
                else:
                    print("error", form.errors)

    fromdate = request.POST.get('fromdate')
    if fromdate:
        context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
        fromdate = fromdate + " 00:00:00"
    else:
        fromdate = str(date.today() - timedelta(days=7)) + " 00:00:00"

    todate = request.POST.get('todate')
    if todate:
        context['to'] = datetime.strptime(todate, "%Y-%m-%d")
        todate = todate + " 23:59:59"
    else:
        todate = str(date.today()) + " 23:59:59"

    context["form"] = form
    context["dataset"] = Transaction.objects.filter(updated_date_time__range=(fromdate, todate),
                                                    yard=request.user.yard).order_by('-updated_date_time')
    return render(request, "stats/deliverynotes2.html", context)


# API for loading details from ajax to editform
glb_trans_data = ''


@login_required(redirect_field_name=None)
def deliverynote_detail(request, identifier):
    try:
        obj = Transaction.objects.get(id=identifier)
    except:
        obj = None
    if obj:
        data = model_to_dict(obj)
        global glb_trans_data
        glb_trans_data = data
    else:
        data = {}
    return JsonResponse(data)


# @login_required(redirect_field_name=None)
def view_images_base64(request, identifier):
    try:
        obj = images_base64.objects.get(transaction_id=identifier)
    except:
        obj = None
    if obj:
        serialized_obj = serialize('json', [obj, ])
        data = json.loads(serialized_obj)[0]['fields']
        return JsonResponse(data)
    else:
        return JsonResponse({'status': False, 'msg': 'No Images'})


@login_required(redirect_field_name=None)
def transaction_update(request):
    context = {}
    # absolute_url = request.build_absolute_uri('?')
    absolute_url = 'http://' + request.get_host()
    context["absolute_url"] = absolute_url
    context['logo'] = Logo.objects.all()
    context['role'] = request.user.role
    context['user_name'] = request.user.name
    context['sign'] = Signature.objects.filter(user=request.user).last()
    context['customer'] = request.session['customer'] if request.session['customer'] else 'Kunde'
    context['article'] = request.session['article'] if request.session['article'] else 'Artikel'
    context['showt'] = ShowTonne.objects.all().last()
    context['io'] = Io.objects.all().last()

    if request.POST:
        id = request.POST.get('id')
        try:
            obj = Transaction.objects.get(id=id)
            form = TransactionForm(request.POST, instance=obj)
            context["images"] = obj.images_base64_set.first
            if form.is_valid():
                obj = form.save()
                context["dataset"] = obj
                context["images"] = obj.images_base64_set.first()
            else:
                print("error", form.errors)
        except:
            obj = None
    return context


@login_required(redirect_field_name=None)
def std_evaluation(request):
    context = {}
    absolute_url = request.build_absolute_uri('?')
    context["absolute_url"] = "http://" + request.get_host()

    if request.POST:
        note_type = request.POST.getlist('note_type')
        stat_type = request.POST.get('stat_type')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        if fromdate:
            context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
            fromdate = fromdate + " 00:00:00"
        else:
            fromdate = str(date.today()) + " 00:00:00"

        if todate:
            context['to'] = datetime.strptime(todate, "%Y-%m-%d")
            todate = todate + " 23:59:59"
        else:
            todate = str(date.today()) + " 23:59:59"
        obj = field_func[stat_type]((fromdate, todate))
        # obj = Transkation.objects.raw('SELECT *,SUM(net_weight) as ttl FROM yard_transkation WHERE created_date_time BETWEEN %s and %s GROUP BY(article_id)',[fromdate,todate])
        if obj:
            if stat_type == 'material' or 'vehicle' or 'supplier' or 'customer':
                # context["data"] = get_article_groupset(obj)
                context['stat_type'] = stat_type
                context['date'] = datetime.now()
                context["data"] = obj
                context["summ"] = sum(j.net_weight for j in obj["transactions"])
                context['head_m'] = request.session['article'] if request.session['article'] else 'Artikel'
                context['head_c'] = request.session['customer'] if request.session['customer'] else 'Kunde'
                context['vehicle'] = 'Fahrzeug'
                context['head_s'] = request.session['supplier'] if request.session['supplier'] else 'Lieferant'
                context['article'] = request.session['article'] if request.session['article'] else 'Artikel'
                return Render.render("stats/pdf/material_stat.html", context)
        else:
            context['error'] = "No Transkations found!"
    # 	article_from = request.POST.get('article_from')
    # 	article_to = request.POST.get('article_to')
    # 	obj = Transaction.objects.filter(created_date_time__range=(fromdate,todate))
    return render(request, "stats/standard_evaluation2.html", context)


@login_required(redirect_field_name=None)
def daily_closing(request):
    context = {}
    absolute_url = request.build_absolute_uri('?')
    context["absolute_url"] = "http://" + request.get_host()
    fromdate = str(date.today()) + " 00:00:00"
    todate = str(date.today()) + " 23:59:59"
    trans = Transaction.objects.filter(trans_flag=1, yard=request.user.yard)
    # trans = Transaction.objects.filter(created_date_time__range=(fromdate,todate),trans_flag=1)
    if len(trans) > 0:
        trans.update(trans_flag=2)
        message = str(len(trans)) + " Transcations Updated"
    else:
        message = "No transcations found!"
    return JsonResponse({'status': True, 'msg': message})


@login_required(redirect_field_name=None)
def site_list(request):
    context = {}
    form = TransactionForm(request.POST or None)
    context["form"] = form
    context["dataset"] = Transaction.objects.filter(trans_flag=0, yard=request.user.yard)
    return render(request, "stats/site_list.html", context)


@login_required
# @user_passes_test(lambda u: u.is_superuser,redirect_field_name=None)
def site_list_delete(request, identifier):
    context = {}
    obj = get_object_or_404(Transaction, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/stats/site_list")


def deliverynote_delete(request, identifier):
    obj = get_object_or_404(Transaction, id=identifier)
    obj.delete()
    return HttpResponseRedirect("/stats/deliverynotes")


@login_required(redirect_field_name=None)
def deliverynotes1(request):
    if 'print_button' in request.POST:
        return pdf_view(request)
    context = {}
    form = TransactionForm(request.POST or None)
    context["form"] = form
    context["dataset"] = Transaction.objects.all().order_by('-updated_date_time')
    return render(request, 'stats/deliverynotes2.html', context)


from django.http import FileResponse, Http404
import os
import sqlite3
import datetime
from datetime import datetime
from django.db import connection

LOGO_DIR = "/var/www/html/pdfdemo"
PDF_DIR = "/var/www/html/pdfdemo"
PDF_BASE_NAME = "delivery_note"
PDF_LATEX = "pdflatex"


def pdf_view(request):
    def R(str):
        if str != None:
            str = str.replace('\\', '\\')
            str = str.replace('$', '\$')
            str = str.replace("`", '``')
            str = str.replace("´", "''")
            str = str.replace('"', "''")
            str = str.replace('<', '$<$')
            str = str.replace('>', '$>$')
            str = str.replace('_', '\\_')
            str = str.replace('#', '\\#')
            str = str.replace('{', '\\{')
            str = str.replace('}', '\\}')
            str = str.replace('^', '\\textasciicircum{}')
            str = str.replace("°", '$^{\\circ}$')
            str = str.replace('€', '\\euro{}')
            str = str.replace('&', '\\&')
            str = str.replace('%', '\\%')
            str = str.replace('Ω', '$\\Omega$')
            str = str.replace('½', '\\sfrac{1}{2}')
            str = str.replace('¾', '\\sfrac{3}{4}')
            str = str.replace('¼', '\\sfrac{1}{4}')
        return str

    def create_sheet(kunde_name, lieferanten_name, artikel_name, kennzeichen, zufahrt_art, weight_info, with_time_var):
        global LOGO_DIR, PDF_LATEX
        global PDF_DIR, PDF_BASE_NAME
        kunden_adresse = R(kunde_name) + ","
        fahrzeugnummer = R(kennzeichen)
        op_ok = True
        op_name = R("my_name")
        op_strasse = R("my_stgreet")
        op_bezeichnung = R("my_description")
        op_plz = R("my_zip")
        op_ort = R("my_town")
        lfd_nr = 1
        the_id = weight_info[0]
        the_weight = int(weight_info[1])
        the_date = weight_info[2]
        if with_time_var:
            the_time = weight_info[3]
        else:
            the_time = ""
        lieferant = "Ab-/Beladestelle\nLieferant:"
        tex_text = "\\documentclass[12pt,oneside,a4paper]{article}\n"
        tex_text += "\\usepackage[utf8]{inputenc}\n"
        tex_text += "\\usepackage[german]{babel}\n"
        tex_text += "\\usepackage{color}\n"
        tex_text += "\\usepackage{eurosym}\n"
        # tex_text += "\\usepackage{xfrac}\n"
        tex_text += "\\pagestyle{empty}\n"
        tex_text += "\\usepackage{graphicx}\n"
        tex_text += "\\usepackage{hyperref}\n"
        tex_text += "\\usepackage[a4paper,left=2cm,right=16mm,top=1cm,bottom=1cm]{geometry}\n"
        tex_text += "\\setlength{\\parindent}{0pt}\n"
        tex_text += "\\begin{document}\n"
        tex_text += "\\begin{sf}\n"
        tex_text += "\\vspace*{4cm}\n"
        tex_text += "\\begin{tabular}{|c|c|c|c|c|c|}\\hline\n"
        tex_text += "\\multicolumn{3}{|p{9cm}|}{\n"
        tex_text += "\\parbox[t]{7cm}{\n"
        tex_text += "\\textbf{\\tiny{" + op_name + "}} \n"
        tex_text += "\\tiny{" + op_bezeichnung + "} "
        tex_text += "\\tiny{" + op_strasse + "}\\\\\n"
        tex_text += "\\tiny{" + op_plz + "} "
        tex_text += "\\tiny{" + op_ort + "}}\n"
        tex_text += "\\parbox[t]{5cm}{\n"
        tex_text += "\\vspace*{5mm}\n"
        tex_text += "\\textbf{\\large %s:}\\\\\n" % ("Kunde")
        if len(kunde_name) > 0:
            print('glb_trans_data', glb_trans_data)
            customer_id = glb_trans_data['customer']
            # cursor = connection.cursor()
            # conn = sqlite3.connect(OPERATOR_DATABASE)
            c = connection.cursor()
            sql_command = "SELECT name, company, street, perm_pin, perm_place FROM yard_customer WHERE id = '%s'" % (
                customer_id)
            #   sql_command = "SELECT vorname, bezeichnung, strasse, PLZ, ort FROM kunden WHERE name = '%s'"%(kunde_name)
            c.execute(sql_command)
            result = c.fetchall()
            connection.close()
            # result = [["Hans", "firma1", "xstreet", "98299", "Boston"]]
            if len(result) > 0:
                tex_text += R(result[0][0]) + " " + R(kunde_name) + "\\\\\n"
                if result[0][1] == None:
                    tex_text += R(str(result[0][1])) + "\\\\\n"
                    kunden_adresse += R(str(result[0][1])) + ","
                else:
                    tex_text += R(result[0][1]) + "\\\\\n"
                    kunden_adresse += R(result[0][1]) + ","
                if result[0][3] == None:
                    tex_text += R(str(result[0][3])) + "\\\\\n"
                    kunden_adresse += R(str(result[0][3])) + ","
                else:
                    tex_text += R(result[0][3]) + "\\\\\n"
                    kunden_adresse += R(result[0][3]) + ","
                if result[0][4] == None:
                    tex_text += R(str(result[0][4])) + "\n"
                    kunden_adresse += R(str(result[0][4])) + "."
                else:
                    tex_text += R(result[0][4]) + "\n"
                    kunden_adresse += R(result[0][4]) + "."
            else:
                tex_text += R(kunde_name) + "\n"
        else:
            tex_text += "\n"
        tex_text += "\\vspace*{5mm}\n"
        tex_text += "}}\n"
        tex_text += "&\\multicolumn{3}{|p{7cm}|}{\n"
        tex_text += "\\vspace*{2mm}\\raisebox{-90pt}{\\includegraphics[width=170pt]{" + LOGO_DIR + "/operator_logo.png}}\n"
        tex_text += "}\\\\ \\hline \n"
        tex_text += "&lfd. Nr.&Datum&Uhrzeit&Werk&Zufuhrart\\\\ \n"
        tex_text += "\parbox{4cm}{"
        tex_text += "\Large Wiegeschein\\\\Lieferschein\\\n\\vspace{2mm}}&%d&%s&%s&&%s\\\\ \\hline\n" % (
            lfd_nr, the_date, the_time, zufahrt_art)
        tex_text += "\\multicolumn{3}{|l|}{%s}&\multicolumn{3}{|l|}{Fahrzeug-Nr.}\\\\ \n" % (lieferant)
        tex_text += "\\multicolumn{3}{|l|}{\n"
        tex_text += "\\parbox{5cm}{\n"
        if len(lieferanten_name) > 0:
            print('glb_trans_data', glb_trans_data)
            supplier_id = glb_trans_data['supplier']
            # cursor = connection.cursor()
            # conn = sqlite3.connect(OPERATOR_DATABASE)
            c = connection.cursor()
            sql_command = "SELECT street, pin, place FROM yard_supplier WHERE id = '%s'" % (supplier_id)
            #        sql_command = "SELECT strasse, plz, ort FROM lieferanten WHERE lieferanten_name = '%s'"%(lieferanten_name)
            c.execute(sql_command)
            result = c.fetchall()
            connection.close()
            # result = [["ystreet", "98932", "berlin"]]
            if len(result) > 0:
                tex_text += "\\vspace{1cm}\n\n"
                tex_text += R(lieferanten_name) + "\\\\\n"
                tex_text += R(result[0][0]) + "\\\\\n"
                tex_text += R(result[0][1]) + " "
                tex_text += R(result[0][2]) + "\\\\\n\n"
            else:
                tex_text += R(lieferanten_name) + "\n"
        tex_text += "}}&\\multicolumn{3}{|l|}{\n"
        tex_text += "\\parbox{5cm}{\n"
        tara = 0
        the_tara_id = "?"
        the_tara_date = "??"
        the_tara_time = "??"
        wstate = ""
        if len(kennzeichen) > 0:
            tex_text += R(kennzeichen) + "\\\\\n\n"
            tara_in_court = False
            print('glb_trans_data', glb_trans_data)
            transaction_id = glb_trans_data['id']
            # cursor = connection.cursor()
            # conn = sqlite3.connect(OPERATOR_DATABASE)
            c = connection.cursor()
            sql_command = "SELECT first_weight, firstw_date_time, firstw_alibi_nr FROM yard_transaction WHERE id = '%s'" % (
                transaction_id)
            # sql_command = "SELECT vehicle_weight, created_date_time, vehicle_weight_id FROM yard_vehicle WHERE id = '%s'"%(vehicle_id)
            # sql_command = "SELECT tara, tara_date, tara_time, tara_id FROM yardlist WHERE kennung = '%s'"%(kennzeichen)
            c.execute(sql_command)
            result = c.fetchall()
            connection.close()
            print('result', result)
            # result = [[1234, "11.02.2021", "11:00", "90"]]
            if len(result) > 0:
                tara_in_court = True
                tara = result[0][0]
                print('tara', tara)
                tara_date = (result[0][1]).date()
                print('tara_date', tara_date)
                the_tara_date = datetime.strftime(tara_date, '%d.%m.%Y')
                print('the_tara_date', the_tara_date)
                the_tara_time = datetime.strftime(result[0][1], "%H:%M")
                print('the_tara_time', the_tara_time)
                the_tara_id = result[0][2]
                if the_tara_date == None:
                    the_tara_date = '???'
                    tara_in_court = False
                if the_tara_time == None:
                    the_tara_time = '???'
                    tara_in_court = False
                if the_tara_id == None:
                    the_tara_id = '?'
                    tara_in_court = False
        #        conn = sqlite3.connect(OPERATOR_DATABASE)
        #        c = conn.cursor()
        #        sql_command = "DELETE FROM yardlist WHERE kennung = '%s'"%(kennzeichen)
        #        c.execute(sql_command)
        #        conn.commit()
        #        conn.close()
        #        if not tara_in_court:
        #            conn = sqlite3.connect(OPERATOR_DATABASE)
        #            c = conn.cursor()
        #            sql_command = "SELECT tara , tara_date, tara_time, tara_id FROM fahrzeuge WHERE kennung = '%s'"%(kennzeichen)
        #            c.execute(sql_command)
        #            result = c.fetchall()
        #            conn.close()
        #            if len(result) > 0:
        #                tara = result[0][0]
        #                the_tara_date = result[0][1]
        #                the_tara_time = result[0][2]
        #                the_tara_id = result[0][3]
        #                if the_tara_date == None:
        #                    the_tara_date = '???'
        #                if the_tara_time == None:
        #                    the_tara_time = '???'
        #                if the_tara_id == None:
        #                    the_tara_id = '?'
        #               wstate = "PT"
        #    else:
        #        tkMessageBox.showinfo('Err','Bitte geben Sie einen ein KFZ-Kennzeichen an!')
        #        return False
        tex_text += "\\vspace*{5mm}\n"
        tex_text += "}}\\\\ \\hline\n"
        tex_text += "\\end{tabular}\n\n"
        tex_text += "\\vspace*{2cm}\n"
        diff = the_weight - tara
        tara_s = str(tara)
        kosten = 0.0
        weight_s = ("%d" % (the_weight)).replace('.', ',')
        if diff >= 0:
            diff_s = ("%d" % (diff)).replace('.', ',')
        else:
            #        conn = sqlite3.connect(OPERATOR_DATABASE)
            #        c = conn.cursor()
            #        sql_command = "UPDATE  fahrzeuge SET tara = '%s' WHERE kennung = '%s'"%(weight_s, kennzeichen)
            #        c.execute(sql_command)
            #        conn.commit()
            #        conn.close()
            diff_s = ("%d" % (-diff)).replace('.', ',')
        #    if with_time_var:
        #        the_tara_date = ""
        #        the_tara_time = ""
        tex_text += "\\begin{tabular}{|p{24mm}p{25mm}p{15mm}p{3mm}rp{1cm}p{40mm}p{14mm}|} \\hline \n"
        tex_text += "&Datum&Uhrzeit&&Gewicht&&%s&Alibi-Nr.\\\\ \\hline \n" % ("Material")
        if diff >= 0:
            tex_text += "Erstwiegung&%s&%s&%s&%s&kg&&%s\\\\ \n" % (
                the_tara_date, the_tara_time, wstate, tara_s, the_tara_id)
            tex_text += "Zweitwiegung&%s&%s&&%s&kg&&%s\\\\ \n" % (the_date, the_time, weight_s, the_id)
        else:
            tex_text += "Zweitwiegung&%s&%s&&%s&kg&&%s\\\\ \n" % (the_date, the_time, weight_s, the_id)
            tex_text += "Erstwiegung&%s&%s&%s&%s&kg&&%s\\\\ \n" % (
                the_tara_date, the_tara_time, wstate, tara_s, the_tara_id)
        tex_text += "Nettogewicht&&&E&%s&kg&%s&\\\\ \\hline \n" % (diff_s, R(artikel_name))
        tex_text += "\\end{tabular}"
        tex_text += "\\vfill\n"
        tex_text += "\\begin{tabular}{|p{53mm}|p{53mm}|p{53mm}|} \\hline\n"
        tex_text += "Unterschrift des Wägers&Unterschrift des Fahrers&Unterschrift des Empfängers\\\\ \hline\n"
        tex_text += "\\rule{0pt}{15mm}&\\rule{0pt}{15mm}&\\rule{0pt}{15mm}\\\\ \\hline\n"
        tex_text += "\\end{tabular}\n\n"
        tex_text += "\\footnotesize{E: errechnet, PT: Preset Tara (voreingegebens Tara)}\\\\\n"
        tex_text += "\\footnotesize{Messwerte aus frei programmierbarer Zusatzeinrichung. Die geeichten Messwerte können eingesehen werden.}\\\\\n"
        tex_text += "\\footnotesize{Für Überladungen haftet der Fahrzeuglenker.}\n"
        tex_text += "\\end{sf}\n"

        tex_text += "\\end{document}\n"
        tex_path = PDF_DIR + "/" + PDF_BASE_NAME + ".tex"
        tfile = open(tex_path, "wb")
        tfile.write(tex_text.encode('utf-8'))
        tfile.close()
        os.system(PDF_LATEX + " -output-directory=" + PDF_DIR + " " + tex_path)

    print('glb_trans_data', glb_trans_data)
    transaction_id = glb_trans_data['id']
    c = connection.cursor()
    sql_command = "SELECT  second_weight, secondw_date_time, secondw_alibi_nr, lfd_nr FROM yard_transaction WHERE id = '%s'" % (
        transaction_id)
    # sql_command = "SELECT tara, tara_date, tara_time, tara_id FROM yardlist WHERE kennung = '%s'"%(kennzeichen)
    c.execute(sql_command)
    result_2 = c.fetchall()
    connection.close()
    print('result_2', result_2)
    # result = [[1234, "11.02.2021", "11:00", "90"]]
    if len(result_2) > 0:
        tara_in_court = True
        tara_2 = result_2[0][0]
        print('tara_2', tara_2)
        tara_date_2 = (result_2[0][1]).date()
        print('tara_date_2', tara_date_2)
        the_tara_date_2 = datetime.strftime(tara_date_2, '%d.%m.%Y')
        print('the_tara_date_2', the_tara_date_2)
        the_tara_time_2 = datetime.strftime(result_2[0][1], "%H:%M")
        print('the_tara_time_2', the_tara_time_2)
        the_tara_id_2 = result_2[0][2]
        lfd_nr = result_2[0][3]

        if the_tara_date_2 == None:
            the_tara_date_2 = '???'
            tara_in_court = False
        if the_tara_time_2 == None:
            the_tara_time_2 = '???'
            tara_in_court = False
        if the_tara_id_2 == None:
            the_tara_id_2 = '?'
            tara_in_court = False

    customer_id = glb_trans_data['customer']
    mycustomer = str(Customer.objects.get(id=customer_id))
    print('mycustomer', mycustomer)

    supplier_id = glb_trans_data['supplier']
    my_supplier = str(Supplier.objects.get(id=supplier_id))
    print('my_supplier', my_supplier)

    article_id = glb_trans_data['article']
    my_article = str(Article.objects.get(id=article_id))
    print('my_article', my_article)

    vehicle_id = glb_trans_data['vehicle']
    my_vehicle = str(Vehicle.objects.get(id=vehicle_id))
    print('my_vehicle', my_vehicle)

    create_sheet(mycustomer, my_supplier, my_article, my_vehicle, lfd_nr,
                 [the_tara_id_2, tara_2, the_tara_date_2, the_tara_time_2], True)
    return FileResponse(open('/var/www/html/pdfdemo/delivery_note.pdf', 'rb'), content_type='application/pdf')


@login_required()
def dump_db_data(request):
    # selected_database = settings.DATABASES["default"]
    # cmd_role = shlex.split(
    #     f"pg_dumpall --dbname=postgresql://{selected_database['USER']}:{selected_database['PASSWORD']}@{selected_database['HOST']}:5432/ --roles-only -f {output_file}")
    # out_cns = subprocess.call(cmd_role)
    # print(out_cns)
    # cmd = f"pg_dump --dbname=postgresql://{selected_database['USER']}:{selected_database['PASSWORD']}@{selected_database['HOST']}:5432/{selected_database['NAME']} -F p  | tee -a {output_file}"
    # out_cns = subprocess.call(cmd, shell=True)
    # print(out_cns)
    # return FileResponse(open(output_file, 'rb'), content_type='application/sql')
    apps = [
        "yard",
        "stats",
        'scale_app',
    ]
    static_dir = os.path.join(os.getcwd(), "stats", "static")
    buf = StringIO()

    os.mkdir(os.path.join(static_dir, "dump"))
    base_dir = os.path.join(static_dir, "dump")

    for app_name in apps:
        buf = StringIO()
        output_file = os.path.join(base_dir, f"{app_name}.xml")
        management.call_command('dumpdata', app_name, "--format", "xml", stdout=buf)
        buf.seek(0)
        with open(output_file, 'w') as f:
            try:
                tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", buf.read()) + "</root>")
                tree = ET.tostring(tree, encoding='utf-8', method='xml')
                f.write(tree.decode("utf8"))
            except Exception as e:
                f.write(buf.read())

    # zip_folder_cmd = shlex.split(f"zip -r {zip_path} {base_dir}/*")
    # out_cns = subprocess.call(zip_folder_cmd, shell=True)

    zip_path = os.path.join(static_dir, "dump.zip")
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # with open(os.path.join(base_dir, file)) as f:
            #     xml = f.read()
            # tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")
            zipf.write(os.path.join(base_dir, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(base_dir)))
    zipf.close()

    zip_file = open(zip_path, 'rb')
    response = FileResponse(zip_file)
    # response = HttpResponse(zip_file, content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="%s"' % 'dump.zip'
    os.remove(zip_path)
    shutil.rmtree(base_dir)
    return response


@csrf_exempt
def import_db(request):
    apps = [
        "yard",
        "stats",
        'scale_app',
    ]
    if request.method == 'POST':
        file = request.FILES["dump_data"]
        file_name = default_storage.save(file.name, file)
        print(file_name)
        base_dir = os.path.join(os.getcwd(), "media")
        target_dir = os.path.join(base_dir, "dump")
        zip_path = os.path.join(base_dir,file.name)
        with zipfile.ZipFile(os.path.join(base_dir, file_name), 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                file_path = os.path.join(target_dir, file)
                management.call_command('loaddata', file_path)

        os.remove(zip_path)
        shutil.rmtree(target_dir)
        return JsonResponse({"status": "Success"}, safe=False)


def special_evaluation(request):
    context = {}

    if request.POST:
        customer = int(request.POST.get('customer'))
        vehicle = int(request.POST.get('vehicle'))
        supplier = int(request.POST.get('supplier'))
        article = int(request.POST.get('article'))
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if fromdate:
            context['from'] = datetime.strptime(fromdate, "%Y-%m-%d")
            fromdate = fromdate + " 00:00:00"
        else:
            context['from'] = datetime.strptime(str(date.today()), "%Y-%m-%d")
            fromdate = str(date.today()) + " 00:00:00"
        if todate:
            context['to'] = datetime.strptime(todate, "%Y-%m-%d")
            todate = todate + " 23:59:59"
        else:
            context['to'] = datetime.strptime(str(date.today()), "%Y-%m-%d")
            todate = str(date.today()) + " 23:59:59"
        try:
            if customer != 0 and vehicle != 0 and supplier != 0 and article != 0:
                obj = Transaction.objects.filter(
                    Q(customer=customer) & Q(vehicle=vehicle) & Q(supplier=supplier) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and vehicle != 0 and supplier != 0:
                obj = Transaction.objects.filter(
                    Q(customer=customer) & Q(vehicle=vehicle) & Q(supplier=supplier)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and supplier != 0 and article != 0:
                obj = Transaction.objects.filter(
                    Q(customer=customer) & Q(supplier=supplier) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and vehicle != 0 and article != 0:
                obj = Transaction.objects.filter(Q(customer=customer) & Q(vehicle=vehicle) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif vehicle != 0 and supplier != 0 and article != 0:
                obj = Transaction.objects.filter(Q(vehicle=vehicle) & Q(supplier=supplier) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and vehicle != 0:
                obj = Transaction.objects.filter(Q(customer=customer) & Q(vehicle=vehicle)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and supplier != 0:
                obj = Transaction.objects.filter(Q(customer=customer) & Q(supplier=supplier)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0 and article != 0:
                obj = Transaction.objects.filter(Q(customer=customer) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif vehicle != 0 and supplier != 0:
                obj = Transaction.objects.filter(Q(vehicle=vehicle) & Q(supplier=supplier)).filter(
                    created_date_time__range=(fromdate, todate))

            elif article != 0 and supplier != 0:
                obj = Transaction.objects.filter(Q(supplier=supplier) & Q(article=article)).filter(
                    created_date_time__range=(fromdate, todate))

            elif customer != 0:
                # obj = Transaction.objects.filter(Q(customer=customer) & Q(vehicle=None) & Q(supplier=None) & Q(article=None)).filter(created_date_time__range=(fromdate, todate))
                obj = Transaction.objects.filter(customer=customer).filter(created_date_time__range=(fromdate, todate))

            elif vehicle != 0:
                # obj = Transaction.objects.filter(Q(customer=None) & Q(vehicle=vehicle) & Q(supplier=None) & Q(article=None)).filter(created_date_time__range=(fromdate, todate))
                obj = Transaction.objects.filter(vehicle=vehicle).filter(created_date_time__range=(fromdate, todate))

            elif supplier != 0:
                # obj = Transaction.objects.filter(Q(customer=None) & Q(vehicle=None) & Q(supplier=supplier) & Q(article=None)).filter(created_date_time__range=(fromdate, todate))
                obj = Transaction.objects.filter(supplier=supplier).filter(created_date_time__range=(fromdate, todate))

            elif article != 0:
                # obj = Transaction.objects.filter(Q(customer=None) & Q(vehicle=None) & Q(supplier=None) & Q(article=article)).filter(created_date_time__range=(fromdate, todate))
                obj = Transaction.objects.filter(article=article).filter(created_date_time__range=(fromdate, todate))
            else:
                obj = None

            # obj = Transaction.objects.filter(Q(customer=customer) & Q(vehicle=vehicle) & Q(supplier=supplier) & Q(article=article)).filter(created_date_time__range=(fromdate, todate))            
            # net_weight = Transaction.objects.filter(customer=int(customer)) | vehicle=int(vehicle)) | supplier=int(supplier)) | article=int(article)).aggregate(Sum('net_weight'))
            net_weight = obj.aggregate(Sum('net_weight'))
            net_weight = net_weight['net_weight__sum']
            print(net_weight)
            context['cust'] = obj
            context['customer'] = request.session['customer'] if request.session['customer'] else 'Kunde'
            context['vehicle'] = 'Fahrzeug'
            context['supplier'] = request.session['supplier'] if request.session['supplier'] else 'Lieferant'
            context['article'] = request.session['article'] if request.session['article'] else 'Artikel'
            context['total_weight'] = net_weight
            context['date'] = datetime.now()
        except Exception as e:
            print(e)
            pass
        if 'pdf' in request.POST:
            return Render.render("stats/pdf/special.html", context)
        if 'excel' in request.POST:
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sonderauswertung')
            row_num = 0
            customer = request.session['customer'] if request.session['customer'] else 'Kunde'
            vehicle = 'Fahrzeug'
            supplier = request.session['supplier'] if request.session['supplier'] else 'Lieferant'
            article = request.session['article'] if request.session['article'] else 'Artikel'
            # heading = ['------', '------', '------', 'Sonderauswertung', '------', '------', '------']
            # for col_num in range(len(heading)):
            #     ws.write(row_num, col_num, heading[col_num])
            # row_num += 2
            columns = ['Datum', 'id', customer, vehicle, supplier, article, 'Gewicht [kg]']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])

            if obj is not None:
                values = obj.values_list('created_date_time', str('id'), 'customer__name1', 'vehicle__license_plate',
                                         'supplier__supplier_name', 'article__name', 'net_weight')

                for row in values:
                    row_num += 1
                    for col_num in range(len(row)):
                        if col_num == 0:
                            ws.write(row_num, col_num, datetime.strftime(row[col_num], "%d.%m.%Y %H:%M"))
                        else:
                            ws.write(row_num, col_num, row[col_num])

                row = 7
                row_num += 2
                for col_num in range(row):
                    if col_num == 5:
                        ws.write(row_num, col_num, 'SUM')
                    if col_num == 6:
                        ws.write(row_num, col_num, net_weight)
            filename = "sonderauswertung %s .xls" % str(date.today())
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename
            wb.save(response)
            return response
    context['customer'] = Customer.objects.all()
    context['vehicle'] = Vehicle.objects.all()
    context['supplier'] = Supplier.objects.all()
    context['article'] = Article.objects.all()
    return render(request, "stats/special_evaluation.html", context)
