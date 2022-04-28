# Generated by Django 3.1.4 on 2022-03-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post_Title', models.CharField(blank=True, max_length=100)),
                ('Date', models.DateField(blank=True)),
                ('Author', models.CharField(blank=True, choices=[('MunchyTeam Moderator', 'MunchyTeam Moderator')], max_length=30)),
                ('Post_Author_MunchySite_Admin_Purposes_Only', models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5)),
                ('Header1', models.CharField(blank=True, max_length=25)),
                ('Paragraph1', models.TextField(blank=True, max_length='500')),
                ('Second_Paragraph', models.TextField(blank=True, max_length='500')),
                ('Header2', models.CharField(blank=True, max_length=25)),
                ('Paragraph2', models.TextField(blank=True, max_length='500')),
                ('Header2_Second_Paragraph', models.TextField(blank=True, max_length='500')),
                ('Header3', models.CharField(blank=True, max_length=25)),
                ('Paragraph3', models.TextField(blank=True, max_length='500')),
                ('Header3_Second_Paragraph', models.TextField(blank=True, max_length='500')),
            ],
        ),
    ]
