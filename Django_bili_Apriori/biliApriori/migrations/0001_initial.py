# Generated by Django 2.2 on 2019-05-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='output_con',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedent_s', models.CharField(max_length=32)),
                ('consequent_s', models.CharField(max_length=32)),
                ('confidence', models.CharField(max_length=32)),
                ('lift', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='output_sup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_s', models.CharField(max_length=32)),
                ('freq', models.CharField(max_length=32)),
            ],
        ),
    ]
