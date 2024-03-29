# Generated by Django 4.2.6 on 2023-12-03 06:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_alter_newsletter_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=2)),
                ('img', models.ImageField(upload_to='product/img')),
            ],
        ),
    ]
