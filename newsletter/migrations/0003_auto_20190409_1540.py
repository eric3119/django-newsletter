# Generated by Django 2.2 on 2019-04-09 18:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_article_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='attachment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to='attachments', verbose_name='attachment'), default=None, size=8),
            preserve_default=False,
        ),
    ]
