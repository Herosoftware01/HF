# Generated by Django 5.2.1 on 2025-06-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electrician', '0003_complaint_assigndept_complaint_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Feedback',
            field=models.CharField(max_length=200),
        ),
    ]
