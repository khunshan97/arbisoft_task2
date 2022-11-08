# Generated by Django 4.1.3 on 2022-11-07 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_questionnaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questionnaire.questionnaire'),
            preserve_default=False,
        ),
    ]
