from django.contrib import admin
from .models import Student
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student

class StudentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'present_class', 'section', 'roll')
    list_filter = ('present_class', 'section')
    resource_class = StudentResource
# Register your models here.
admin.site.register(Student,StudentAdmin)