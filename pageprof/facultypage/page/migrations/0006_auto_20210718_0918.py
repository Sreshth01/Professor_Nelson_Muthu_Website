# Generated by Django 2.2.17 on 2021-07-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20210717_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='special_position',
            field=models.CharField(blank=True, help_text='e.g course coordinator etc', max_length=100),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
