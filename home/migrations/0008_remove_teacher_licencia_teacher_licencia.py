# Generated by Django 4.2.7 on 2023-11-28 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_teacher_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='licencia',
        ),
        migrations.AddField(
            model_name='teacher',
            name='licencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.licencia'),
        ),
    ]
