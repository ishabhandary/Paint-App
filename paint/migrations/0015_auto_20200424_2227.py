# Generated by Django 3.0.5 on 2020-04-24 16:57

from django.db import migrations, models
import paint.validators


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0014_auto_20200414_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_consists_of',
            name='Quantity',
            field=models.IntegerField(validators=[paint.validators.nonneg], verbose_name='Quantity'),
        ),
    ]
