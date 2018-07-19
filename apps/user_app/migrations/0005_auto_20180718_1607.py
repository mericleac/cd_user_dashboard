# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-18 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20180718_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_reg_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_dashboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_messages', to='login_reg_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_posted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='login_reg_app.User'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]