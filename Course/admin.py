from django.contrib import admin
from . import models
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Name',)}
    list_display = ['Name', 'slug']
    
admin.site.register(models.Type, TypeAdmin)

admin.site.register(models.AddCourse)
admin.site.register(models.Comment)
admin.site.register(models.EnrolledCourse)