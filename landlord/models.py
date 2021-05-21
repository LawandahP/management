from django.db import models
from utils.models import TimeStamps
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Landlord(TimeStamps, models.Model):
    Full_Name = models.CharField(max_length=255)
    GENDER = (
        ('Male', ('Male')),
        ('Female', ('Female')),
        ('Unspecified', ('Unspecified')),
    )
    gender = models.CharField(choices=GENDER,
                              default='Male',
                              max_length=15)

    email = models.EmailField()
    National_ID = models.IntegerField(verbose_name='ID No.')
    phone_number1 = PhoneNumberField(unique=True, region='KE',
                                     verbose_name='phone number')

    phone_number2 = PhoneNumberField(unique=True,
                                     region='KE',
                                     verbose_name='Emergency Contact')
    post_office_box = models.CharField(max_length=255,
                                       help_text='e.g P.O BOX 481-800100, Mombasa',
                                       unique=True, blank=True)

    def __str__(self):
        return self.Full_Name.upper()
