# Generated by Django 4.2.7 on 2023-11-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('aceptada', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('rut', models.CharField(max_length=9)),
                ('especialidad', models.CharField(max_length=50)),
                ('dias_presente', models.IntegerField(max_length=100)),
                ('dias_ausente', models.IntegerField(max_length=100)),
                ('asignatura', models.ManyToManyField(to='home.asignaturas')),
                ('licencia', models.ManyToManyField(to='home.licencia')),
            ],
        ),
    ]