# Generated by Django 4.0.4 on 2022-11-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_text', models.TextField(help_text='Enter a brief description of your entry', max_length=400)),
                ('reminder_date', models.DateTimeField(verbose_name='date to be reminded')),
                ('event_date', models.DateTimeField(verbose_name='date of event')),
            ],
        ),
    ]
