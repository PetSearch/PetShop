# django imports
from django.db import models

DISCOUNT_TYPE_CHOICES = (
    ('Flat', 'Flat'),
    ('Percentage', 'Percentage'),
)

STATUS_FIELD_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Expired', 'Expired'),
)


class Coupon(models.Model):
    code = models.CharField(verbose_name="Coupon Code", max_length=255, unique=True, null=False)
    description = models.TextField(default=None)
    discount_type = models.CharField(verbose_name="Discount Type", choices=DISCOUNT_TYPE_CHOICES, default='Flat', null=False, max_length=15)
    discount_value = models.DecimalField(verbose_name="Discount Value", decimal_places=2, max_digits=10, default=0)
    valid_from = models.DateField(verbose_name="Valid From",)
    valid_till = models.DateField(verbose_name="Valid Till",)
    status = models.CharField(verbose_name="Satus", choices=STATUS_FIELD_CHOICES, default='Active', null=False, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "coupon"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return self.code
