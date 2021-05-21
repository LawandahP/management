from django.db import models

# Create your models here.
from landlord.models import Landlord
from utils.models import TimeStamps


class Apartment(TimeStamps, models.Model):
    county_list = (
        ('Mombasa', 'Mombasa'),
        ('Kwale', ('Kwale')),
        ('Kilifi', ('Kilifi')),
        ('Tana River', ('Tana River')),
        ('Lamu', ('Lamu')),
        ('Taita Taveta', ('Taita Taveta')),
        ('Garissa', ('Garissa')),
        ('Wajir', ('Wajir')),
        ('Mandera', ('Mandera')),
        ('Marsabit', ('Marsabit')),
        ('Isiolo', ('Isiolo')),
        ('Meru', ('Meru')),
        ('Tharaka-Nithi', ('Tharaka-Nithi')),
        ('Embu', ('Embu')),
        ('Kitui', ('Kitui')),
        ('Machakos', ('Machakos')),
        ('Makueni', ('Makueni')),
        ('Nyandarua', ('Nyandarua')),
        ('Nyeri', ('Nyeri')),
        ('Kirinyaga', ('Kirinyaga')),
        ('Muranga', ('Muranga')),
        ('Kiambu', ('Kiambu')),
        ('Turkana', ('Turkana')),
        ('West Pokot', ('West Pokot')),
        ('Samburu', ('Samburu')),
        ('Uasin Gishu', ('Uasin Gishu')),
        ('Trans Nzoia', ('Trans Nzoia')),
        ('Elgeyo-Marakwet', ('Elgeyo-Marakwet')),
        ('Nandi', ('Nandi')),
        ('Baringo', ('Baringo')),
        ('Laikipia', ('Laikipia')),
        ('Nakuru', ('Nakuru')),
        ('Narok', ('Narok')),
        ('Kajiado', ('Kajiado')),
        ('Kericho', ('Kericho')),
        ('Bomet', ('Bomet')),
        ('Kakamega', ('Kakamega')),
        ('Vihiga', ('Vihiga')),
        ('Bungoma', ('Bungoma')),
        ('Busia', ('Busia')),
        ('Siaya', ('Siaya')),
        ('Kisumu', ('Kisumu')),
        ('Homa Bay', ('Homa Bay')),
        ('Migori', ('Migori')),
        ('Kisii', ('Kisii')),
        ('Nyamira', ('Nyamira')),
        ('Nairobi', ('Nairobi')),
        ('choose county..', ('choose county..')),
    )
    type_apartment = (
        ('Bungalow', ('Bungalow')),
        ('Apartment', ('Apartment')),
        ('Maisonette', ('Maisonette')),
        ('GroundFloor', ('GroundFloor')),
        ('Condos', ('Condos')),
    )
    name = models.CharField(max_length=255,
                            unique=True)

    type = models.CharField(max_length=255,
                            default='choose county..',
                            choices=type_apartment)

    county = models.CharField(max_length=255,
                              default='Apartment',
                              choices=county_list)

    location = models.CharField(help_text='E.g. Shepherd',
                                max_length=255)

    location_description = models.CharField(max_length=30, help_text='E.g. Near Brookside Depot',
                                            blank=True, verbose_name='Location Description(Optional)')

    owner = models.ForeignKey(Landlord,
                              on_delete=models.CASCADE,
                              related_name='owner')

    def __str__(self):
        return self.name.upper()

    class Meta:
        ordering = ['name']
