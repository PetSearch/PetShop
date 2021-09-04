from django.contrib import admin
from django.utils.safestring import mark_safe
from coupon.models import Coupon


class CouponDetailsAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'valid_from', 'valid_till', 'status')
    list_display_links = ("code",)
    search_fields = ("order_number", "discount_value")
    list_filter = ("status", "discount_type")
    fields = (('code',), ('discount_type', 'discount_value'), ('valid_from', 'valid_till', 'status'), 'description')
    icon_name = 'exposure'


admin.site.register(Coupon, CouponDetailsAdmin)
