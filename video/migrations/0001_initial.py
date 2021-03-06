# Generated by Django 3.1.3 on 2020-11-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_date', models.DateField()),
                ('vid_title', models.CharField(max_length=20)),
                ('vid_url', models.URLField()),
                ('vid_code', models.CharField(max_length=4)),
                ('vid_intro', models.CharField(max_length=100)),
                ('vid_cap_trans', models.CharField(max_length=100)),
                ('vid_lines_trans', models.CharField(max_length=100)),
                ('vid_axis_prd', models.CharField(max_length=100)),
                ('vid_cover_prd', models.CharField(max_length=100)),
                ('vid_sup_prd', models.CharField(max_length=100)),
                ('admin', models.EmailField(max_length=254)),
            ],
        ),
    ]
