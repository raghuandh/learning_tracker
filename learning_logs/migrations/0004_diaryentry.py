# Generated by Django 5.0.1 on 2024-02-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.TextField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]