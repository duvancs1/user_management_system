# Generated by Django 4.2.10 on 2024-03-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
