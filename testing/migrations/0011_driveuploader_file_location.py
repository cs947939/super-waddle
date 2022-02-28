# Generated by Django 4.0.2 on 2022-02-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0010_alter_driveuploader_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='driveuploader',
            name='File_Location',
            field=models.CharField(blank=True, choices=[('-----', '-----'), ('OneDrive', 'OneDrive'), ('Dropbox', 'Dropbox'), ('Google Drive', 'Google Drive')], max_length=20),
        ),
    ]