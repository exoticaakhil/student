# Generated by Django 4.2.6 on 2023-11-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdapp', '0007_remove_student_hobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Hobby',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
