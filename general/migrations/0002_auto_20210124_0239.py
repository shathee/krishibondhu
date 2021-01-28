# Generated by Django 3.1.5 on 2021-01-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='lat',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='lon',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]