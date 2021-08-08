from django.core.files.storage import FileSystemStorage
from django.db import models
from rest_framework import serializers


def create_path(instance, filename):
    flag = True
    if flag:
        path = f'hamid/behzad/{filename}'
    else:
        path = f'hamid/milad/{filename}'

    return path


# Create your models here.


class Spent(models.Model):
    spent_amount = models.IntegerField()
    spent_date = models.DateTimeField(auto_now=True)
    spent_description = models.TextField()


class Image(models.Model):
    image_path = models.ImageField(upload_to=create_path)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        return super(Image, self).save(force_insert=False, force_update=False, using=None,
                                       update_fields=None)
