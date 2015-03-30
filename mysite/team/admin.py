from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Team
from easy_thumbnails.files import get_thumbnailer


class TeamAdmin(ImageCroppingMixin, admin.ModelAdmin):
    readonly_fields = ('image_url', 'thumb_url',)

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            kwargs['fields'] = ['name', 'position', 'original_image_width',
                                'original_image_height', 'facebook_url',
                                'twitter_url', 'google_url','tumblr_url',
                                'github_url', 'OSF_url', 'linkedin_url',
                                'personal_Email', 'personal_web', 'image', ]
            kwargs['exclude'] = ['image_url', 'thumb_url', ]
        else:
            kwargs['fields'] = ['name', 'position', 'original_image_width',
                                'original_image_height', 'facebook_url',
                                'twitter_url', 'google_url', 'tumblr_url',
                                'github_url', 'OSF_url', 'linkedin_url',
                                'personal_Email', 'personal_web', 'image',
                                'thumb_image_width', 'thumb_image_height',
                                'min_free_cropping', 'image_url', 'thumb_url', ]
        return super(TeamAdmin, self).get_form(request, obj, **kwargs)

    def image_url(self, obj):
        if not obj.image:
            return 'make sure you click on save and continue editing button before you click save'
        return '<a target="_blank" href="' + obj.image.url + '">' + obj.image.url + '</a>'
    image_url.allow_tag = True

    def thumb_url(self, obj):
        if not obj.image or not obj.thumb_image_width or not obj.thumb_image_height:
            return 'make sure you click on save and continue editing button before you click save'
        url = get_thumbnailer(obj.image).get_thumbnail({
            'size': (obj.thumb_image_width, obj.thumb_image_height),
            'box': obj.min_free_cropping,
            'crop': True,
            'detail': True,
            }).url
        return '<a target="_blank" href="' + url + '">' + url + '</a>'
    thumb_url.allow_tag = True

admin.site.register(Team, TeamAdmin)




