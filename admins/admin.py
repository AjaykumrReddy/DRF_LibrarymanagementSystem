from django.contrib import admin
from .models import AdminRegistration, Library
# Register your models here.


class AdminRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'password')


class LibraryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'desc'
    )


admin.site.register(AdminRegistration, AdminRegistrationAdmin)
admin.site.register(Library, LibraryAdmin)
