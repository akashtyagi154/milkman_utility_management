# Generated by Django 3.2.7 on 2021-09-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk_CRM', '0007_alter_customer_sale_data_unpaid_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customersdata',
            name='rates',
        ),
        migrations.AlterField(
            model_name='milk_transaction',
            name='customer',
            field=models.CharField(choices=[('again', 'again')], max_length=20),
        ),
    ]
