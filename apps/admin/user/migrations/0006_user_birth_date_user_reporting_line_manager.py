# Generated by Django 4.2.10 on 2024-03-02 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='1996-01-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='reporting_line_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
