# Generated by Django 4.1 on 2022-09-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_avatar_username_alter_avatar_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.CharField(default=333, max_length=200),
            preserve_default=False,
        ),
    ]