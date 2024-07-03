from django.contrib import admin
from main import models
from django.urls import reverse
from django.utils.html import format_html


admin.site.register(models.Informations)


@admin.register(models.Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'detail', 'price', 'edit_link', 'delete_link']
    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True
    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'edit_link', 'delete_link']
    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True
    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True


@admin.register(models.Baner)
class BanerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'detail', 'edit_link', 'delete_link']
    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'email', 'phone_number', 'text', 'edit_link', 'delete_link']

    def edit_link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-edit" href="{}"> Edit</a>', url)
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a class="button fa fa-trash" href="{}"> Delete</a>', url)
    delete_link.short_description = 'Delete'
    delete_link.allow_tags = True




