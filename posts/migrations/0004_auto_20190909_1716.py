# Generated by Django 2.1.5 on 2019-09-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190909_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]
