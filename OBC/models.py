from django.db import models
import datetime

class Student(models.Model):

    year_dropdown = []
    for y in range((datetime.datetime.now().year -10), (datetime.datetime.now().year+1)):
        year_dropdown.append((y, y))

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    CLASS_CHOICES = [
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X')
    ]

    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B')
    ]

    name = models.CharField(max_length=60)
    fathers_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Select Gender')
    date_of_birth = models.DateField()
    last_class_passed = models.CharField(max_length=4, choices=CLASS_CHOICES)
    year_of_passing = models.IntegerField(choices=year_dropdown, default=datetime.datetime.now().year-1)
    present_class = models.CharField(max_length=4, choices=CLASS_CHOICES)
    section = models.CharField(max_length=4, choices=SECTION_CHOICES)
    roll = models.CharField(max_length=2)
    annual_family_income = models.CharField(max_length=6)
    village = models.CharField(max_length=25)
    post_office = models.CharField(max_length=25)
    sub_division = models.CharField(max_length=25)
    block = models.CharField(max_length=25)
    pincode = models.CharField(max_length=6)
    mobile_number = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=45)
    branch_name = models.CharField(max_length=25)
    ifsc_code = models.CharField(max_length=20)
    account_no = models.CharField(max_length=30)
    sub_caste = models.CharField(max_length=25)

    def __str__(self):
        return f'Data of {self.name} Added'
