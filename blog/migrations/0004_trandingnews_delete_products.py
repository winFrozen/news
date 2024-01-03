# Generated by Django 4.2.6 on 2023-11-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trandingnews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('explain', models.TextField()),
                ('data', models.DateTimeField()),
                ('img', models.ImageField(upload_to='News/img')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
