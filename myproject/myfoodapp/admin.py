from django.contrib import admin
from myfoodapp.models import *
from django.utils.html import format_html

# Register your models here.
admin.site.register(Kid)

class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.img_url.url))

    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']

admin.site.register(Image, GalleryAdmin)
