# Generated by Django 4.2.7 on 2023-11-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_descriiption_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='exit', upload_to='file'),
            preserve_default=False,
        ),
    ]