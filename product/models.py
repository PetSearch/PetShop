from django.db import models
import os

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


def image_upload_path_category(instance, filename):
    return os.path.join("images", "category", filename)


def image_upload_path_item(instance, filename):
    return os.path.join("images", "item", filename)


class Category(models.Model):
    title = models.CharField(max_length=100)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload_path_category, verbose_name="Category Image", null=True, blank=True)

    class Meta:
        db_table = "product_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="User", related_name="item", null=False, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload_path_item, verbose_name="Item Image", null=True, blank=True)

    class Meta:
        db_table = "product_category_item"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title
