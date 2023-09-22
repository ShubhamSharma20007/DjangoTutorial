# Generated by Django 4.2 on 2023-09-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=52)),
                ('description', models.CharField(max_length=102)),
                ('picture', models.ImageField(upload_to='testimonial')),
                ('rating', models.IntegerField()),
            ],
        ),
    ]