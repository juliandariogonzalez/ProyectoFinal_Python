# Generated by Django 4.2.3 on 2023-08-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inversiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa', models.CharField(max_length=20)),
                ('ambientes', models.IntegerField()),
                ('localidad', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
