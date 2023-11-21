# Generated by Django 4.2.4 on 2023-11-21 00:12

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': True,
            },
            bases=(models.Model, core.models.AuditableModelMixin),
        ),
    ]
