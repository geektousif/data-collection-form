from django.forms import ModelForm
from .models import Student
from django.utils.translation import gettext as _
from django.forms import TextInput,NumberInput,RadioSelect,DateInput

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {'sub_caste':_('Sub Caste(Jaat)')}
        widgets = { 
            'name': TextInput(attrs={
                'class': 'w-full bg-gray-200 text-black border border-gray-200 rounded py-3 px-4 mb-3',
                'placeholder': 'Student\'s Name'
            }),
             'fathers_name': TextInput(attrs={
                'class': 'w-full bg-gray-200 text-black border border-gray-200 rounded py-3 px-4 mb-3',
                'placeholder': 'Father\'s Name'
            }),
            'gender': RadioSelect(attrs={
                'choices' : Student.GENDER_CHOICES,
                'class' : ''
            }),
            'date_of_birth' : DateInput(format=('%d-%m-%Y'), 
                attrs={'class':'w-full bg-gray-200 text-black border border-gray-200 rounded py-3 px-4 mb-3 datepicker', 
                        'placeholder':'Select a date'})
        }