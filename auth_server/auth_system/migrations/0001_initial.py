# Generated by Django 3.0.3 on 2020-03-19 06:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSessions',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('app_id_1', models.CharField(max_length=50)),
                ('app_id_2', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=100)),
                ('refresh_token', models.CharField(max_length=100)),
                ('token_born', models.CharField(max_length=100)),
            ],
        ),
    ]