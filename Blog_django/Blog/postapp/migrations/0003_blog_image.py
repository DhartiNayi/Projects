# Generated by Django 4.1.4 on 2023-08-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_remove_blog_image_remove_blog_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='postapp/'),
        ),
    ]
