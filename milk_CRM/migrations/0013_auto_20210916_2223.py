# Generated by Django 3.2.7 on 2021-09-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk_CRM', '0012_auto_20210916_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='milk_transaction',
            name='customer1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='milk_transaction',
            name='customer',
            field=models.CharField(choices=[('Himanshu', 'Himanshu'), ('Kamal', 'Kamal'), ('Akash', 'Akash'), ('new_test_customer', 'new_test_customer'), ('again', 'again'), ('Murari', 'Murari')], max_length=20),
        ),
        migrations.AlterField(
            model_name='payment_transact',
            name='customer',
            field=models.CharField(choices=[('Himanshu', 'Himanshu'), ('Kamal', 'Kamal'), ('Akash', 'Akash'), ('new_test_customer', 'new_test_customer'), ('again', 'again'), ('Murari', 'Murari')], max_length=20),
        ),
    ]
