from django.apps import AppConfig


class CouponConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coupon'
    verbose_name = 'Coupon'
    icon_name = 'redeem'
