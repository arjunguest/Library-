# Generated by Django 2.2 on 2022-03-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_picture'),
        ),
    ]
