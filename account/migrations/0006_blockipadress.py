# Generated by Django 5.2.1 on 2025-06-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_ips'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockIpAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]
