# Generated by Django 5.0.4 on 2024-05-03 00:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_comment_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(verbose_name='Comment Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.meal'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
