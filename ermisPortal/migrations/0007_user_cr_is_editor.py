# Generated by Django 2.1 on 2019-09-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ermisPortal', '0006_user_kb_is_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cr_is_editor',
            field=models.BooleanField(default=False),
        ),
    ]
