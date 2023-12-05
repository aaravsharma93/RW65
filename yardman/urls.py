from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from yard.api import VehicleView, CustomerView, SupplierView, ArticleView, BuildingSiteView, WarehouseView, \
    TransactionView, TransactView, CombinationView, CombinationReadView

router = routers.DefaultRouter()

router.register("Vehicle-View", VehicleView, basename='vehicle'),
router.register("customer-View", CustomerView, basename='customer'),
router.register("supplier-View", SupplierView, basename='supplier'),
router.register("article-View", ArticleView, basename='article'),
router.register("buildingsite-View", BuildingSiteView, basename='buildingsite'),
router.register("Warehouse-View", WarehouseView, basename='warehouse')
router.register("Transactions", TransactionView, basename='transaction')
router.register("transact", TransactView, basename='transact')
router.register("ID", CombinationView, basename='Combination')
router.register("IDRead", CombinationReadView, basename='CombinationRead')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yard.urls')),
    path('yard/', include('django.contrib.auth.urls')),
    path('stats/', include('stats.urls')),
    path('', include('scale_app.urls')),
    path('api/', include(router.urls)),
    # path('api/transact/', TransactView.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('', include('agri.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

