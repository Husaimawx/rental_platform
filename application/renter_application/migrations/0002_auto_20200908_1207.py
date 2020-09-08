# Generated by Django 3.1.1 on 2020-09-08 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('renter_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renterapplication',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='renter_applications', to='user.user'),
        ),
    ]