# Generated by Django 3.1.6 on 2021-03-25 08:24

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0003_auto_20210325_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text'),
        ),
    ]
