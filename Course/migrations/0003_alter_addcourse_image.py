# Generated by Django 5.0.1 on 2024-01-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_addcourse_comment_enrolledcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Course/media/uploads/'),
        ),
    ]
