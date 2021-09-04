from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coupon import views

router = DefaultRouter()
router.register(r'coupons', views.CouponViewSet, basename="api_coupons")

urlpatterns = [
    path('', include(router.urls)),
]
