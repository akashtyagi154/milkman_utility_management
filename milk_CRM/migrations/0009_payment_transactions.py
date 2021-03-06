# Generated by Django 3.2.7 on 2021-09-16 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milk_CRM', '0008_auto_20210916_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(choices=[('again', 'again')], max_length=20)),
                ('payment_amount', models.IntegerField(blank=True, null=True)),
                ('payment_time', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='milk_CRM.customer_sale_data')),
            ],
        ),
    ]
