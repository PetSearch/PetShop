from django.contrib import admin
from django.utils.safestring import mark_safe
from product.models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'label')
    list_display_links = ("title",)
    # search_fields = ("name", "id")
    # list_filter = ("name", "status", "featured")
    fields = (('title',), 'description', ('label', ), 'category_image')
    icon_name = 'face'
    readonly_fields = ["category_image"]
    # fieldsets = [
    #     (None, {'fields': ['id', 'name', 'image']}),
    #     ('Advance information', {'fields': ['status', 'featured', 'created_at', 'updated_at'], 'classes':['collapse']}),
    # ]

    def category_image(self, obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url,))

    def img(self, obj):
        return mark_safe('<img src="{url}",  width="50px" height="50px" />'.format(url=obj.image.url))


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'price', 'discount_price', 'category', 'label')
    list_display_links = ("title",)
    # search_fields = ("name", "id")
    # list_filter = ("name", "status", "featured")
    fields = (('title', 'category'), 'description', 'label', ('price', 'discount_price'), 'item_image')
    icon_name = 'face'
    readonly_fields = ["item_image"]
    # fieldsets = [
    #     (None, {'fields': ['id', 'name', 'image']}),
    #     ('Advance information', {'fields': ['status', 'featured', 'created_at', 'updated_at'], 'classes':['collapse']}),
    # ]

    def item_image(self, obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url,))

    def img(self, obj):
        return mark_safe('<img src="{url}",  width="50px" height="50px" />'.format(url=obj.image.url))


admin.site.register(Item, ItemAdmin)
