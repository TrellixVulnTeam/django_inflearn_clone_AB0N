# Generated by Django 3.1.4 on 2020-12-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0003_auto_20201224_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]