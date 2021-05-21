# Generated by Django 3.1.1 on 2021-01-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid')], default='unpaid', max_length=255),
        ),
    ]
