# Generated by Django 4.1 on 2022-08-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, upload_to='images')),
                ('cUrl', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eFname', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=254)),
                ('ePhone', models.CharField(max_length=50)),
                ('eCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.company')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
