# Generated by Django 4.0.2 on 2023-01-26 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/blogs')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
