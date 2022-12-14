# Generated by Django 3.2 on 2022-11-11 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('postalZip', models.IntegerField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(max_length=50)),
                ('acc_num', models.CharField(max_length=50)),
                ('pan', models.CharField(max_length=50)),
                ('cvv', models.IntegerField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
            ],
        ),
    ]
