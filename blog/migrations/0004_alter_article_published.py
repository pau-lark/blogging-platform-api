# Generated by Django 4.0.2 on 2022-02-12 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 10, 14, 4, 57748, tzinfo=utc)),
        ),
    ]
