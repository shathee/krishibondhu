# Generated by Django 3.1.5 on 2021-01-28 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bn_name', models.CharField(blank=True, max_length=15, null=True)),
                ('lat', models.TextField(blank=True, max_length=50, null=True)),
                ('lon', models.TextField(blank=True, max_length=50, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('metropolitan', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bn_name', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='1', max_length=15)),
                ('bn_name', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bn_name', models.CharField(blank=True, max_length=15, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('district', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='general.district')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.division'),
        ),
    ]
