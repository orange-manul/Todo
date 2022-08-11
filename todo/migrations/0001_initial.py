# Generated by Django 4.0.6 on 2022-08-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('memo', models.TextField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]