# Generated by Django 4.1 on 2022-09-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_options_project_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.CharField(default='', max_length=200, verbose_name='Subtítulo'),
        ),
    ]
