# Generated by Django 4.1.3 on 2023-03-10 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_company_user_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PHONE', 'Phone'), ('TABLET', 'Tablet'), ('LAPTOP', 'Laptop')], default='PHONE', max_length=6)),
                ('name', models.CharField(max_length=200)),
                ('available_status', models.CharField(choices=[('AVAILABLE', 'Available'), ('NOT_AVALIABLE', 'Not Available')], default='AVAILABLE', max_length=13)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.company')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_condition', models.CharField(max_length=500, null=True)),
                ('post_condition', models.CharField(blank=True, max_length=500, null=True)),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.company')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.device')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
