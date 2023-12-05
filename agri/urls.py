from django.urls import path
from agri import views

urlpatterns = [
    # Agriculure #
    path('agriculture_home', views.agriculture_home, name="agriculture_home"),
    path('crop', views.crop, name="crop"),
    path('crop_add', views.crop_add, name="crop_add"),
    path('crop_view', views.crop_view, name="crop_view"),
    path('crop_delete', views.crop_delete, name="crop_delete"),

    path('add_uom/', views.add_uom, name="add_uom"),

    path('crop_location/', views.crop_location, name="crop_location"),
    path('crop_location_add/', views.crop_location_add, name="crop_location_add"),
    path('crop_location_edit/<id>', views.crop_location_edit,
         name="crop_location_edit"),
    path('crop_location_delete/<id>', views.crop_location_delete,
         name="crop_location_delete"),

    path('crop_cycle/', views.crop_cycle_list, name="crop_cycle"),
    path('crop_cycle_add/', views.crop_cycle_add, name="crop_cycle_add"),
    path('crop_cycle_edit/<id>/', views.crop_cycle_edit, name="crop_cycle_edit"),

    path('plant_analysis/', views.plant_analysis_list, name="plant_analysis_list"),
    path('plant_analysis_add/', views.plant_analysis_add,
         name="plant_analysis_add"),
    path('plant_analysis_delete/', views.plant_analysis_delete,
         name="plant_analysis_delete"),
    path('plant_analysis_edit/<id>', views.plant_analysis_edit,
         name="plant_analysis_edit"),

    # path('add_criteria/',views.add_criteria, name="add_criteria"),
    # path('delete_criteria/',views.delete_criteria, name="delete_criteria"),

    path('soil_analysis/', views.soil_analysis_list, name="soil_analysis_list"),
    path('soil_analysis_add/', views.soil_analysis_add, name="soil_analysis_add"),
    path('soil_analysis_edit/<id>', views.soil_analysis_edit,
         name="soil_analysis_edit"),
    path('soil_analysis_delete', views.soil_analysis_delete,
         name="soil_analysis_delete"),

    path('soil_texture/', views.soil_texture_list, name="soil_texture_list"),
    path('soil_texture_add/', views.soil_texture_add, name="soil_texture_add"),
    path('soil_texture_edit/<id>', views.soil_texture_edit,
         name="soil_texture_edit"),
    path('soil_texture_delete', views.soil_texture_delete,
         name="soil_texture_delete"),

    path('weather', views.weather, name="weather"),
]
