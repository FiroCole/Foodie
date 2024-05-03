# Generated by Django 5.0.4 on 2024-05-02 21:54

import django.db.models.deletion
from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_commenting',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=timezone.now, verbose_name='Comment Date'),
        ),
        migrations.AddField(
            model_name='comment',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.meal'),
        ),
        migrations.AddField(
            model_name='meal',
            name='location',
            field=models.ManyToManyField(to='main_app.location'),
        ),
        migrations.AddField(
            model_name='meal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.user'),
        ),
    ]