__author__ = 'zobair'
from django.db import models
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from image_cropping import ImageCropField


class Job(models.Model):
    background = models.CharField(max_length=500, null=True)
    core_technologies = models.CharField(max_length=500, null=True)
    skills = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=500, null=True)
    benefits = models.CharField(max_length=500, null=True)
    applying = models.CharField(max_length=1000, null=True)
    responsibilities = models.CharField(max_length=500, null=True)
    referrals = models.TextField()

    class Meta:
        verbose_name_plural = u'COS Jobs Section'







