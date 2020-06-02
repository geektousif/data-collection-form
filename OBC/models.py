from django.db import models
import datetime

year_dropdown = []
for y in range(2011, (datetime.datetime.now().year + 5)):
    year_dropdown.append((y, y))

class Student(models.Model):
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
    year_of_passing = models.IntegerField(_('year'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year-1)
    current_class = models.CharField(max_length=4, choices=CLASS_CHOICES)
    section = models.CharField(max_length=4, choices=SECTION_CHOICES)
    roll = models.PositiveSmallIntegerField()
    annual_family_income = models.PositiveIntegerField()
    village = models.CharField(max_length=25)
    post_office = models.CharField(max_length=25)
    sub_division = models.CharField(max_length=25)
    block = models.CharField(max_length=25)
    district = models.CharField(max_length=15)
    pincode = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=45)
    branch_name = models.CharField(max_length=25)
    ifsc_code = models.CharField(max_length=20)
    account_no = models.CharField(max_length=30)