# Generated by Django 3.1.2 on 2020-10-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20201020_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applicant', to='api.staff'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='belongs_to', to='api.staff'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='date',
            field=models.DateField(),
        ),
    ]