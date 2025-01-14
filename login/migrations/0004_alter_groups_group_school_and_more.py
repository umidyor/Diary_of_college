# Generated by Django 5.0.6 on 2024-05-13 00:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_groups_group_teacher_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='group_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.school'),
        ),
        migrations.AlterField(
            model_name='pupils',
            name='pupil_username',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pupil_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
