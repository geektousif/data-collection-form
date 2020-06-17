import django_filters
from OBC.models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['present_class', 'section']