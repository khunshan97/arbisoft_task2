# Generated by Django 4.1.3 on 2022-11-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('questions', models.ManyToManyField(blank=True, to='questionnaire.question')),
            ],
        ),
    ]
