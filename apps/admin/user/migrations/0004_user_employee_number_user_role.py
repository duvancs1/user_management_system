# Generated by Django 4.2.10 on 2024-03-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(0, 'None'), (1, 'Backend Developer'), (2, 'Frontend Developer'), (3, 'Full-stack Developer'), (4, 'DevOps Engineer'), (5, 'UI/UX Designer'), (6, 'QA Engineer'), (7, 'Project Manager')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
