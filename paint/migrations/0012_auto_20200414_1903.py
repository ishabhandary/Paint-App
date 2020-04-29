# Generated by Django 3.0.4 on 2020-04-14 13:33

from django.db import migrations, models
import paint.validators


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0011_auto_20200414_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Date_of_joining',
            field=models.DateField(validators=[paint.validators.datevalid], verbose_name='Date Of Joining'),
        ),
    ]
