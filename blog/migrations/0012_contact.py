# Generated by Django 4.2.6 on 2023-11-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_status_alter_categorynews_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('massage', models.TextField()),
            ],
        ),
    ]