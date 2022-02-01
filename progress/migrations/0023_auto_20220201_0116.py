# Generated by Django 3.2.11 on 2022-02-01 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0022_alter_messages_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='Time_Of_Response',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='From',
            field=models.CharField(choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=100),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Message',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='messages',
            name='Response',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='messages',
            name='To',
            field=models.CharField(choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=100),
        ),
    ]