from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from yard import views
from yard import management_views
from .utils.view_handling import changelanguage
from .views import scale_data

# from django.contrib.admin.views.decorators import staff_member_required
# from .forms import UserLoginForm
urlpatterns = [
    path('', views.home, name='home'),
    path('ss_home/', views.self_service_home, name='ss_home'),
    path('scale_data/', scale_data, name='scale_data'),
    path('settings/', management_views.settings, name='settings'),
    path('test_smtp/', management_views.test_smtp_connection, name='test_smtp'),
    path('save_smtp/', management_views.save_smtp_connection, name="save_smtp"),

    path('vehicle/', management_views.vehicle, name='vehicle'),
    path('vehicle_detail/<identifier>', management_views.vehicle_detail, name="vehicle_detail"),
    path('vehicle_delete/<identifier>', management_views.vehicle_delete, name="vehicle_delete"),
    path('vehicle_list/', management_views.vehicle_list, name='vehicle_list'),
    path('vehicle_save/', management_views.vehicle_save, name='vehicle_save'),
    # path('vehicle_list_json/', views.vehicle_list_json, name='vehicle_list_json'),

    path('customer/', management_views.customer, name='customer'),
    path('customer_details/<identifier>', management_views.customer_details, name="customer_details"),
    path('customer_delete/<identifier>', management_views.customer_delete, name="customer_delete"),
    path('customer_list/', management_views.customer_list, name='customer_list'),
    # path('customer_list_json/', views.customer_list_json, name='customer_list_json'),

    path('supplier/', management_views.supplier, name='supplier'),
    path('supplier_detail/<identifier>', management_views.supplier_detail, name="supplier_detail"),
    path('supplier_delete/<identifier>', management_views.supplier_delete, name="supplier_delete"),
    path('supplier_list/', management_views.supplier_list, name='supplier_list'),
    # path('supplier_list_json/', views.supplier_list_json, name='supplier_list_json'),

    path('forwarders/', management_views.forwarders, name='forwarders'),
    path('forwarders_detail/<identifier>', management_views.forwarders_detail, name="forwarders_detail"),
    path('forwarders_delete/<identifier>', management_views.forwarders_delete, name="forwarders_delete"),

    # path('transkation/', views.transkation, name='transkation'),
    # path('transkation_detail/<identifier>', views.transkation_detail, name="transkation_detail"),
    # path('transkation_delete/<identifier>', views.transkation_delete, name="transkation_delete"),

    path('yard_list/', views.yard_list, name='yard_list'),
    path('yard_list_detail/<identifier>', views.yard_list_detail, name="yard_list_detail"),
    path('yard_list_delete/<identifier>', views.yard_list_delete, name="yard_list_delete"),
    path('yard_creation/', views.yard_creation, name="yard_creation"),

    path('article/', views.article, name='article'),
    path('article_detail/<identifier>', views.article_detail, name="article_detail"),
    path('article_delete/<identifier>', views.article_delete, name="article_delete"),
    path('article_list/', views.article_list, name='articleList'),
    # path('article_list_json/', views.article_list_json, name='article_list_json'),

    path('building_site/', views.building_site, name='building_site'),
    path('building_site_detail/<identifier>', views.building_site_detail, name="building_site_detail"),
    path('building_site_delete/<identifier>', views.building_site_delete, name="building_site_delete"),

    path('container/', views.container, name='container'),
    path('container_details/<identifier>', views.container_details, name="container_details"),
    path('container_delete/<identifier>', views.container_delete, name="container_delete"),
    path('container_list/', views.container_list, name='container_list'),

    path('delivery_note/', views.delivery_note, name='delivery_note'),
    path('delivery_note_detail/<identifier>', views.delivery_note_detail, name="delivery_note_detail"),
    path('delivery_note_delete/<identifier>', views.delivery_note_delete, name="delivery_note_delete"),

    path('combination/<identifier>', management_views.combination, name="combination"),
    # path('kombinationen/save/', views.kombinationen_save, name="save-kombi"),

    # path('sign_up/', views.sign_up, name="sign_up"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('sign_out/', views.sign_out, name="sign_out"),
    # path('sign_in/',auth_views.LoginView.as_view(template_name="yard/login.html",authentication_form=UserLoginForm),name='sign_in'),
    # path('login/', auth_views.LoginView.as_view(template_name="yard/login.html"), name='login'),

    path('users_list/', views.users_list, name='users_list'),
    path('user_edit/', views.user_edit, name='user_edit'),
    path('users_details/<identifier>', views.users_details, name="users_details"),
    path('user_delete/<identifier>', views.user_delete, name="user_delete"),

    path('pdf_template/', views.transaction_save, name='pdf_template'),

    # index page popups
    path('customer_popup/', views.customer_popup, name='customer_popup'),
    path('material_popup/', views.material_popup, name='material_popup'),
    path('vehicle_popup/', views.vehicle_popup, name='vehicle_popup'),
    path('supplier_popup/', views.supplier_popup, name='supplier_popup'),
    path('change/<str:lang>', changelanguage, name='Change'),
    path('transcation_popup/', views.transcation_popup, name='transcation_popup'),
    path('transcation_detail/<identifier>', views.transcation_detail, name="transcation_detail"),

    path('warehouse/', management_views.warehouse, name='warehouse'),
    path('warehouse_detail/<identifier>', management_views.warehouse_detail, name="warehouse_detail"),
    path('warehouse_delete/<identifier>', management_views.warehouse_delete, name="warehouse_delete"),
    path('warehouse_list/', management_views.warehouse_list, name='warehouseList'),

    # self service users urls
    path('ss_users/', views.get_ss_user, name='ss_users'),
    path('ss_get_fields/<int:id>', views.get_auth_ss_fields, name='ss_get_fields'),
    path('ss_update_field/', views.update_ss_field, name='update_ss_field'),
    path('get_field_values/', views.get_field_values, name="get_field_values"),
    #
    path('logo/', management_views.logo, name='logo'),
    path('sign/', management_views.sign, name='sign'),
    path('comb_list/', management_views.comb_list, name='comb_list'),
    path('comb_delete/<identifier>', management_views.comb_delete, name='comb_delete'),
    path('e_sign/', management_views.e_sign, name='e_sign'),
    path('schrank/', management_views.schrank, name='schrank'),
    path('copy/', management_views.copy, name='copy'),
    path('adv_set/', management_views.advance_set, name='adv_set'),
    path('foreign_list/', management_views.foreign_list, name='foreign_list'),
    path('foreign_list_delete/<identifier>', management_views.foreign_list, name='foreign_list_delete'),
    path('auto_capture/', management_views.auto_capture, name='auto_capture'),

    # Contract urls
    path('contract/<contract_number>', management_views.get_contract, name='contracts'),
    path('contracts/', management_views.ContractView.as_view(), name='crud_contract'),
    path('update_contract/', management_views.update_contract, name='update_contract'),
    path('contract_pdf/<contract_number>', management_views.contract_pdf, name='contract_pdf'),

    path('silo/', management_views.Silo_view.as_view(), name='silo'),
    path('material_quality/<int:_id>/', management_views.material_quality, name='material_quality'),
    path('material_quality_delete/', management_views.material_quality_delete, name='material_quality_delete'),
    path('schlag_detail/<int:_id>/', management_views.schlag_detail, name='schlag_detail'),
    path('sclag_delete/', management_views.sclag_delete, name='sclag_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
