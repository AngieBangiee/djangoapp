# Generated by Django 3.1 on 2022-04-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mtpPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(max_length=100)),
                ('meta_description', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
