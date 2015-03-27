from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import News
from easy_thumbnails.files import get_thumbnailer
from suit.admin import SortableModelAdmin


class NewsAdmin(ImageCroppingMixin, SortableModelAdmin):
    readonly_fields = ('image_url', 'thumb_url',)
    sortable = 'order'

    def image_url(self, obj):
        if not obj.image:
            return '';
        return '<a target="_blank" href="' + obj.image.url + '">' + obj.image.url + '</a>'
    image_url.allow_tag = True

    def thumb_url(self, obj):
        if not obj.image or not obj.thumb_image_width or not obj.thumb_image_height:
            return ''
        url = get_thumbnailer(obj.image).get_thumbnail({
                'size': (obj.thumb_image_width, obj.thumb_image_height),
                'box': obj.min_free_cropping,
                'crop': True,
                'detail': True,
                }).url
        return '<a target="_blank" href="' + url + '">' + url + '</a>'
    thumb_url.allow_tag = True

admin.site.register(News, NewsAdmin)