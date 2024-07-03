# Generated by Django 5.0.6 on 2024-07-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_image_alter_baner_background_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]
