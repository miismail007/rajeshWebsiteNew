# Generated by Django 3.2.5 on 2022-03-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20220325_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
