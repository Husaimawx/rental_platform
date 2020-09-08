# Generated by Django 3.1.1 on 2020-09-08 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('equipment', '0002_auto_20200908_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='current_tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rented_equipments', to='user.user'),
        ),
    ]