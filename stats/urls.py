from django.urls import path
from django.conf.urls.static import static
from yard import views
from stats import views

urlpatterns = [
    path('special_evaluation/', views.special_evaluation, name='special_evaluation'),
    path('std_evaluation/', views.std_evaluation, name='std_evaluation'),
    path('deliverynotes/', views.deliverynotes, name='deliverynotes'),
    path('send_deliverynotes/<trans_id>', views.send_delivery_note, name="send_delivery_note"),

    path('deliverynote_delete/<identifier>', views.deliverynote_delete, name="deliverynote_delete"),
    # path('deliverynotes/', views.deliverynotes, name='deliverynotes'),
    path('deliverynote_detail/<identifier>', views.deliverynote_detail, name="deliverynote_detail"),
    path('view_images_base64/<identifier>', views.view_images_base64, name="view_images_base64"),

    path('daily_delivery_list/', views.daily_delivery_list, name='daily_delivery_list'),
    path('daily_closing/', views.daily_closing, name='daily_closing'),
    path('site_list/', views.site_list, name='site_list'),
    path('site_list_delete/<identifier>', views.site_list_delete, name="site_list_delete"),
    path('data_dump/', views.dump_db_data, name="dump_data"),
    path('import_data/', views.import_db, name="import_data")
]
