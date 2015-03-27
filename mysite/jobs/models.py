__author__ = 'zobair'
from django.db import models
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField, ImageCropField


class Job(models.Model):
    background = models.CharField(max_length=500, null=True)
    Core_Technologies = models.CharField(max_length=500, null=True)
    Skills = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=500, null=True)
    benefits = models.CharField(max_length=500, null=True)
    Applying = models.CharField(max_length=1000, null=True)
    Responsibilities = models.CharField(max_length=500, null=True)
    Referrals = models.TextField()

    class Meta:
        verbose_name_plural = u'COS Jobs Section'







