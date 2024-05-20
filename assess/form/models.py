from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import re


# Create your models here.
def validate_letters(value):
  if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")


class Student(models.Model):

  COURSE_CHOICES =[
        ('certificate in health science', 'Certificate in Health Science'),
        ('certificate in applied technology', 'Certificate in Applied Technology'),
        ('bachelor of inforamtion technology', 'Bachelor of Inforamtion Technology'),
        ('bachelor in business technology', 'Bachelor of Business Technology'),
        ('master of public health', 'Master of Public Health'),

    ]
  ENTRY_SCHEME_CHOICES = [
        ('a-level certificate','A-Level Certificate'),
        ('adult/mature learning','Adult/Mature Learning'),
        ('certificate', 'Certificate'),
        ('diploma','Diploma'),
        ('bachelors','Bachelors'),
    ]
  INTAKE_CHOICES = [
        ('january intake','January Intake'),
        ('may intake','May Intake'),
        ('august intake','August'),
    ]
  SPONSOR_CHOICES = [
        ('private','Private'),
        ('government','Government'),
        ('bursary','Bursary'),
    ]
  GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
    ] 

  first_name = models.CharField(validators=[MinLengthValidator(3),validate_letters],max_length=50, blank=True, null=True)
  last_name = models.CharField(validators=[MinLengthValidator(3),validate_letters],max_length=50, blank=True, null=True)
  course = models.CharField(max_length=50,blank=True, null=True, choices=COURSE_CHOICES)
  entry_scheme = models.CharField(max_length=50,blank=True, null=True, choices=ENTRY_SCHEME_CHOICES)
  intake = models.CharField(max_length=50,blank=True, null=True, choices=INTAKE_CHOICES)
  sponsorship = models.CharField(max_length=50,blank=True, null=True, choices=SPONSOR_CHOICES)
  gender = models.CharField(max_length=50,blank=True, null=True, choices=GENDER_CHOICES, default="male")
  date_of_birth = models.CharField(max_length=50, blank=True, null=True)
  residence = models.CharField(max_length=255, blank=True, null=True)

  