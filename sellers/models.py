from django.db import models
from django.contrib.auth.models import User
from django.core import validators
import os

# Create your models here.
GENDER_FIELD_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


def image_upload_path(instance, filename):
    return os.path.join("images", "sellers", filename)


class SellerProfile(models.Model):
    seller = models.ForeignKey(User, verbose_name="Sellers", related_name="sellers", null=False, on_delete=models.CASCADE)
    storeName = models.CharField(verbose_name="Store Name", null=False, max_length=50,
                                 help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                 validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    image = models.ImageField(upload_to=image_upload_path, verbose_name="eller Image", null=True, blank=True)
    gender = models.CharField(verbose_name="Gender", choices=GENDER_FIELD_CHOICES, null=False, max_length=15)
    regDate = models.DateField(verbose_name="Date of Registration")
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "seller_profile"
        verbose_name = "Seller Profile"
        verbose_name_plural = "Seller Profiles"

    def __str__(self):
        return f'{self.storeName}'
