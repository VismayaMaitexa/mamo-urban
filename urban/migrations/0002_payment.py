# Generated by Django 5.0 on 2024-10-17 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('card_number', models.CharField(max_length=16)),
                ('account_holder_name', models.CharField(max_length=100)),
                ('cvv', models.CharField(max_length=3)),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urban.booking')),
            ],
        ),
    ]
