from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sellers import views

router = DefaultRouter()
router.register(r'sellerprofile', views.SellerProfileViewSet, basename="api_sellerprofiles")
router.register(r'seller', views.SellerViewSet, basename="api_seller")


urlpatterns = [
    path('', include(router.urls)),
]
