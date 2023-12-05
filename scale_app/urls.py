from django.urls import path
from django.conf.urls.static import static
from scale_app.views import *

urlpatterns = [
	# path('', views.home, name='home'),
	path('scaleview/', Home.as_view(),),
	# path('scale_data/', scale_data, name='scale_data'),
	path('devices/', DevicesList.as_view(), name='devices'),
	path('edit_devices/<idd>', EditDevices.as_view(), name='edit_devices'),
	path('activate_device/<idd>', ActivateDevice.as_view(), name='activate_device'),
	path('delete_device/<idd>', DeleteDevice.as_view(), name='delete_device'),
	path('set_tara/', SetTara.as_view(), name='set_tara'),
	path('trans_list/<idd>', TransList.as_view(), name='trans_list'),
	path('login/',login, name='login'),
	path('logout/',logout, name='logout'),

]
