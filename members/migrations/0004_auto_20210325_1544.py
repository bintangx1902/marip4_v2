# Generated by Django 3.1.6 on 2021-03-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210325_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile/img/'),
        ),
    ]
