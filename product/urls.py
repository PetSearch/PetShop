from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register(r'product-category', views.CategoryViewSet, basename="api_productcategory")
router.register(r'product-category-item', views.ItemViewSet, basename="api_productitem")

urlpatterns = [
    path('', include(router.urls)),
]
