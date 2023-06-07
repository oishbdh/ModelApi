# Generated by Django 2.2.4 on 2023-06-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('First_Name', 'First_Name'), ('Last_Name', 'Last_Name')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('employed', models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semi_Urban', 'Semi_Urban'), ('Urban', 'Urban')], max_length=50)),
                ('graduated', models.CharField(choices=[('Graduated', 'Graduated'), ('Not_Graduated', 'Not_Graduated')], max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('revenue', models.IntegerField(default=0)),
                ('marital_status', models.BooleanField(choices=[('Single', 'Single'), ('Divorced', 'Divorced'), ('Married', 'Married')], default=None)),
            ],
        ),
    ]
