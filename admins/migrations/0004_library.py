# Generated by Django 3.2.14 on 2022-07-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_auto_20220713_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
    ]
