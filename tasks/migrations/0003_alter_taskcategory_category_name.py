# Generated by Django 3.2 on 2021-05-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_task_category_taskcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='category_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
