from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views import View
import json
import socket
import time
import sys
import _thread
from .forms import *
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login ,logout
#from django.views.decorators.clickjacking import xframe_options_exempt




the_socket = None
class Home(View):
	#@xframe_options_exempt
	def get(self, request):
		# <view logic>
		context={}
		# x = scale_data()
		try:
			obj = Devices.objects.filter(active=True).first()
			if obj:
				context["data"]=obj
		except:
			context["data"]=None
		return render(request, "scale_app/home.html",context)
	def post(self, request,*args, **kwargs):
		context={}
		try:
			tara = request.POST.get("tara_val")
			weight = request.POST.get("load")
			dev_id = Devices.objects.filter(active=True).first()
			obj=Transaction()
			obj.device=dev_id
			obj.tara=float(tara.strip())
			obj.net_weight=float(weight.strip())
			obj.save()
		except Exception as e:
			print ("Exception",e)
			pass
		return JsonResponse(context)


class EditDevices(View):
	def get(self, request,idd):
		if not request.session["authenticated"]:
			return HttpResponseRedirect("/login")
		# <view logic>
		try:
			obj = Devices.objects.filter(id=idd).first()
		except:
			obj=None
		if obj:
			form = DevicesForm(instance=obj)
		else:
			form=DevicesForm()
		context={}
		context["form"]=form
		context["idd"]=idd
		return render(request, "scale_app/info.html",context)

	def post(self, request,*args, **kwargs):
		if not request.session["authenticated"]:
			return HttpResponseRedirect("/login")
		try:
			id=request.POST.get("id")
			obj = Devices.objects.filter(id=id).first()
		except:
			obj=None
		if obj:
			form = DevicesForm(request.POST, instance=obj)
		else:
			form = DevicesForm(request.POST)
		if form.is_valid():
		    form.save()
		    # <process form cleaned data>
		    return HttpResponseRedirect('/devices/')

		return render(request, "scale_app/info.html", {'form': form})


def scale_data(request):
	global W_MESSAGE, IT1_IP_ADDR, IT1_PORT
	global the_socket
	try:
		tara1 = request.GET.get("tara")
	except:
		tara1 = 0
	x10 = request.GET.get("x10")
	request.session["tara1"] = tara1
	W_MESSAGE = "<RM>"
	
	try:
		obj = Devices.objects.filter(active=True).first()
		if obj.ip_addr:
			IT1_IP_ADDR = str(obj.ip_addr)
		if obj.port:
			IT1_PORT = str(obj.port)
	except:
		IT1_IP_ADDR = "109.90.104.232"
		print(IT1_IP_ADDR)
		IT1_PORT = "3200"
	try:
	    if the_socket == None:
	        the_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        the_socket.settimeout(5.0)
	        the_socket.connect(( IT1_IP_ADDR, int(IT1_PORT) ))

	    the_socket.send(W_MESSAGE.encode("UTF-8"))
	    time.sleep(0.2)
	    chunks = []
	    d = the_socket.recv(1)
	    while d:
	        chunks.append(d)
	        d = the_socket.recv(1)
	        if ord(d) == ord('\r'):
	            d = the_socket.recv(1)
	            if ord(d) == ord('\n'):
	                break;
	    data = b''.join(chunks)
	    data = str(data, 'utf-8')
	except:
	    the_socket.close()
	    the_socket = None
	    return None
	print ("received: " + data)
	time.sleep(0.2)
	error_info = data[1:3]
	still = data[3:4]
	brutto_stat = data[4:5]
	date_str = data[5:13]
	date_str = date_str.replace('/', '.')
	timestr = data[13:18]
	#   # print ("timestr = " + timestr + ", fehler = " + fehler + ", ruhe = " + ruhe + ", brutto_stat = " + brutto_stat + ", date = " + date_str)
	ident = data[18:22]
	waanr = data[22:23]
	brutto = data[23:31]
	tara = data[31:39]
	netto = data[39:47]
	unit = data[47:49]
	sn_num = data[58:63]
	try:
		brutto = int(brutto)-int(tara1)
	except Exception as e:
		print ("exception",e)
		brutto = data[23:31]
	if x10=="1":
		brutto = float(brutto)
	data = {"sn_num":sn_num,"still":still,"unit":unit,"tara":tara,"msg_type":"weight", "state":"good", "alibi_nr" : ident, "weight" : str(brutto), "date" : date_str, "time" :  timestr}
	print(data)
	return JsonResponse(data)


class DevicesList(View):
	def get(self, request):
		try:
			if not request.session["authenticated"]:
				return HttpResponseRedirect("/login")
		except:
				return HttpResponseRedirect("/login")
			
		try:
			obj = Devices.objects.all()
		except:
			obj=None
		context={}
		context["dataset"]=obj
		return render(request, "scale_app/devices.html",context)


class ActivateDevice(View):
	def get(self, request,idd):
		if not request.session["authenticated"]:
			return HttpResponseRedirect("/login")
		try:
			active_dev = Devices.objects.filter(active=True).first()
			active_dev.active=False
			active_dev.save()
			new_active = Devices.objects.filter(id=idd).first()
			new_active.active=True
			new_active.save()			
		except Exception as e:
			new_active = Devices.objects.filter(id=idd).first()
			new_active.active=True
			new_active.save()
			print ("Error",e)
			obj=None
		context={}
		context["dataset"]=Devices.objects.all()
		return render(request, "scale_app/devices.html",context)


class DeleteDevice(View):
	def get(self, request,idd):
		if not request.session["authenticated"]:
			return HttpResponseRedirect("/login")
		obj = get_object_or_404(Devices,id=idd)
		obj.delete()			
		context={}
		return HttpResponseRedirect("/devices")

class SetTara(View):
	def get(self, request):
		try:
			tara = float(request.GET.get('tara1'))
		except:
			tara = 0
		request.session["tara1"] = tara
		data = {"tara1":tara}
		return JsonResponse(data)


class TransList(View):
	def get(self, request,idd):
		if not request.session["authenticated"]:
			return HttpResponseRedirect("/login")
		context={}
		try:
			obj = get_object_or_404(Devices,id=idd)
			trans_list = Transaction.objects.filter(device=obj).all()
		except Exception as e:
			print ("Errorrrrrrr",e)
			obj = None
			trans_list = []
		context["dataset"]=trans_list
		return render(request, "scale_app/trans_list.html",context)



def login(request):
	context={}
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				print ("user authenticated")
				request.session["authenticated"] = True
				return HttpResponseRedirect("/devices/")
			else:
				return HttpResponseRedirect("/login")
		except Exception as e:
			return HttpResponseRedirect("/login")
	form = LoginForm()
	context["form"] = form
	return render(request, "scale_app/login.html",context)


def logout(request):
	request.session["authenticated"] = False
	return HttpResponseRedirect("/")









		
