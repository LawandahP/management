from django.db import models
from unit.models import Unit
from users.models import CustomUser
from utils.models import TimeStamps


class Bill(TimeStamps, models.Model):
    STATUS = (
        ('paid', ('paid')),
        ('unpaid', ('unpaid')),
    )
    unit = models.ForeignKey(Unit, max_length=10, null=True,
                             on_delete=models.PROTECT,
                             related_name='unit_bills')
    bill = models.CharField(max_length=255, blank=False)
    amount = models.IntegerField()
    status = models.CharField(max_length=255, choices=STATUS,
                              default='unpaid')

    def __str__(self):
        return f'{self.bill}'
