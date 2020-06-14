from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'present_class', 'section', 'roll')
    list_filter = ('present_class', 'section')
# Register your models here.
admin.site.register(Student,StudentAdmin)