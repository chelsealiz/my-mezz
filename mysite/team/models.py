# coding=utf-8
import os
from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.CharField(max_length=255)

    original_image_width = models.PositiveIntegerField(null=True)
    original_image_height = models.PositiveIntegerField(null=True)

    thumb_image_width = models.PositiveIntegerField(null=True)
    thumb_image_height = models.PositiveIntegerField(null=True)

    image = ImageCropField(upload_to='uploaded_images')
    min_free_cropping = ImageRatioField('image', free_crop=True)

    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    google_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    OSF_url = models.CharField(max_length=255, null=True, blank=True)
    personal_Email = models.CharField(max_length=255, null=True, blank=True)
    personal_web = models.CharField(max_length=255, null=True, blank=True)
    tumblr_url = models.CharField(max_length=255, null=True, blank=True)
    #tumblr_url2 = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_thumb_max_size(self):
        return str(self.thumb_image_width) + 'x' + str(self.thumb_image_height);

    def save(self, *args, **kwargs):
        found_id = self.id
        super(Team, self).save(*args, **kwargs)
        if self.image and found_id is None and self.original_image_width and self.original_image_height:
            print '123'
            self.image = get_thumbnailer(self.image).get_thumbnail({
                'size': (self.original_image_width, self.original_image_height),
            }).name
        super(Team, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = u'Add COS Team Images Here'
        verbose_name = u'COS'








