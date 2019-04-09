# Generated by Django 2.2 on 2019-04-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20190409_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='attachments',
        ),
        migrations.AddField(
            model_name='article',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='attachment/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
