# Generated by Django 5.0.6 on 2024-05-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_subjectgroupschedule_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectgroupschedule',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Dushanba'), ('Tuesday', 'Seshanba'), ('Wednesday', 'Chorshanba'), ('Thursday', 'Payshanba'), ('Friday', 'Juma'), ('Saturday', 'Shanba')], max_length=10),
        ),
    ]
