# Generated by Django 4.1.7 on 2023-04-24 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_blogpost_remove_commentdc_liked_delete_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
