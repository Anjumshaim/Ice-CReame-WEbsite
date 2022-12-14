# Generated by Django 2.1 on 2022-11-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('address2', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('zip', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
