# Generated by Django 4.0.6 on 2022-08-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
