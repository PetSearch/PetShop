from django.contrib import admin
from django.utils.safestring import mark_safe
from sellers.models import SellerProfile


class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('seller', 'storeName', 'img', 'regDate', 'gender')
    list_display_links = ("seller",)
    # search_fields = ("name", "id")
    # list_filter = ("name", "status", "featured")
    fields = (('seller',), 'image', ('regDate', 'gender'), 'seller_image')
    icon_name = 'face'
    readonly_fields = ["seller_image"]
    # fieldsets = [
    #     (None, {'fields': ['id', 'name', 'image']}),
    #     ('Advance information', {'fields': ['status', 'featured', 'created_at', 'updated_at'], 'classes':['collapse']}),
    # ]

    def seller_image(self, obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url,))

    def img(self, obj):
        return mark_safe('<img src="{url}",  width="50px" height="50px" />'.format(url=obj.image.url))


admin.site.register(SellerProfile, SellerProfileAdmin)
