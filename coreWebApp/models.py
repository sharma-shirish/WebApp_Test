from django.db import models


# Create your models here.
class Company(models.Model):
    logo = models.ImageField(upload_to='static/img/')
    name = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    address_number = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_zip = models.IntegerField
    address_state = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Companies'
