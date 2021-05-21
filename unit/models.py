from django.db import models

# Create your models here.
from django.utils import timezone

from apartment.models import Apartment
from users.models import CustomUser
from utils.models import TimeStamps


class Unit(TimeStamps, models.Model):
    type_house = (
        ('SINGLE', ('SINGLE')),
        ('DOUBLE', ('DOUBLE')),
        ('BEDSITTER', ('BEDSITTER')),
        ('ONE BEDROOM', ('ONE BEDROOM')),
        ('TWO BEDROOM', ('TWO BEDROOM')),
        ('THREE BEDROOM', ('THREE BEDROOM')),
        ('MANSIONETTE', ('MANSIONETTE')),
        ('SHOP', ('SHOP')),
        ('STORE', ('STORE'))
    )
    vacancy = (
        ('vacant', ('vacant')),
        ('occupied', ('occupied')),
    )
    select_apartment = models.ForeignKey(Apartment,
                                         on_delete=models.CASCADE,
                                         related_name='in_apartment')
    unit_no = models.CharField(max_length=10, unique=True)
    unit_type = models.CharField(max_length=255, default='ONE BEDROOM', choices=type_house)
    rent = models.IntegerField(verbose_name='Monthly Rent(Kshs)')
    confirm_allocation = models.BooleanField(default=False)
    tenant = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                               max_length=255, null=True,
                               related_name='takenTenants', unique=True)

    amount = models.IntegerField(null=True)
    deposit = models.IntegerField(default=0)
    rent_paid = models.IntegerField(default=0)
    placement_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.unit_no}'

    class Meta:
        ordering = ['created_at']


class AllocateTenantUnit(models.Model):
    type_house = (
        ('SINGLE', ('SINGLE')),
        ('DOUBLE', ('DOUBLE')),
        ('BEDSITTER', ('BEDSITTER')),
        ('ONE BEDROOM', ('ONE BEDROOM')),
        ('TWO BEDROOM', ('TWO BEDROOM')),
        ('THREE BEDROOM', ('THREE BEDROOM')),
        ('MANSIONETTE', ('MANSIONETTE')),
        ('SHOP', ('SHOP')),
        ('STORE', ('STORE'))
    )

    select_apartment = models.ForeignKey(Apartment,
                                         on_delete=models.CASCADE,
                                         related_name='takenApartment')
    unit_no = models.CharField(max_length=10, unique=True)
    unit_type = models.CharField(max_length=255, default='ONE BEDROOM', choices=type_house)
    rent = models.IntegerField(verbose_name='Monthly Rent(Kshs)', null=True)
    tenant = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                               max_length=255, null=True, unique=True)
    deposit = models.IntegerField(default=0)
    rent_paid = models.IntegerField(default=0)
    placement_date = models.DateField(default=timezone.now)
    confirm_allocation = models.BooleanField(default=True, help_text='Check to confirm')

    def __str__(self):
        return f'{self.unit_no}'


class VacateTenant(models.Model):
    type_house = (
        ('SINGLE', ('SINGLE')),
        ('DOUBLE', ('DOUBLE')),
        ('BEDSITTER', ('BEDSITTER')),
        ('ONE BEDROOM', ('ONE BEDROOM')),
        ('TWO BEDROOM', ('TWO BEDROOM')),
        ('THREE BEDROOM', ('THREE BEDROOM')),
        ('MANSIONETTE', ('MANSIONETTE')),
        ('SHOP', ('SHOP')),
        ('STORE', ('STORE'))
    )

    select_apartment = models.ForeignKey(Apartment,
                                         on_delete=models.CASCADE,
                                         related_name='takeApartment')
    unit_no = models.CharField(max_length=10, unique=True)
    unit_type = models.CharField(max_length=255, default='ONE BEDROOM', choices=type_house)
    tenant = models.OneToOneField(CustomUser, on_delete=models.PROTECT,
                                  max_length=255, null=True)
    confirm_allocation = models.BooleanField(default=False, verbose_name='Uncheck to '
                                                                         'vacate '
                                                                         'tenant')

    def __str__(self):
        return f'{self.unit_no}'



