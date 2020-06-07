from django.forms import ModelForm
from .models import Student
from django.utils.translation import gettext as _
from django.forms import TextInput,NumberInput,RadioSelect, Select

form_class = 'w-full bg-gray-200 text-black border border-gray-200 rounded py-3 px-4 mb-3'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {'sub_caste':_('Sub Caste(Jaat)')}
        widgets = { 
            'name': TextInput(attrs={
                'class': form_class,
                'placeholder': 'Student\'s Name'
            }),
             'fathers_name': TextInput(attrs={
                'class': form_class,
                'placeholder': 'Father\'s Name'
            }),
            'gender': RadioSelect(attrs={
                'choices' : Student.GENDER_CHOICES,
                'class' : ' bg-gray-200 text-black border border-gray-200 rounded'
            }),
            'date_of_birth' : TextInput( 
                attrs={'class':'w-full bg-gray-200 text-black border border-gray-200 rounded py-3 px-4 mb-3 datepicker', 
                        'placeholder':'Select a date',
                        'id':'example' 
                        }),
            'last_class_passed': Select(choices=Student.CLASS_CHOICES,attrs={'class': form_class}),
            'year_of_passing': Select(choices=Student.year_dropdown,attrs={'class': form_class}),
            'present_class': Select(choices=Student.CLASS_CHOICES,attrs={'class': form_class}),
            'section': Select(choices=Student.SECTION_CHOICES,attrs={'class': form_class}),
            'roll': TextInput(attrs={'class': form_class, 'placeholder' : 'Roll'}),
            'annual_family_income': TextInput(attrs={'class': form_class, 'placeholder' : 'Annual Family Income'}),
            'village': TextInput(attrs={'class': form_class, 'placeholder' : 'Village'}),
            'post_office': TextInput(attrs={'class': form_class, 'placeholder' : 'Post Office'}),
            'sub_division': Select(attrs={'id':"listBox" ,'onchange':'selct_block(this.value)', 'class':form_class}),
            'block': Select(attrs={'id':"secondlist" , 'class':form_class}),
            'pincode': TextInput(attrs={'class': form_class, 'placeholder' : 'Pincode'}),
            'mobile_number': TextInput(attrs={'class': form_class, 'placeholder' : 'Mobile Number'}),
            'sub_caste': TextInput(attrs={'class': form_class, 'placeholder' : 'Sub-Caste(Jaat)'}),
            'bank_name': Select(attrs={'id':"banks" , 'class':form_class}),
            'branch_name': TextInput(attrs={'placeholder':'Branch Name' , 'class':form_class}),
            'ifsc_code': TextInput(attrs={'placeholder':'IFSC Code' , 'class':form_class}),
            'account_no': TextInput(attrs={'placeholder':'Account No.' , 'class':form_class}),
            
        }