# Generated by Django 4.2.6 on 2023-12-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('YR', 'Yaroqli'), ('YS', 'Yaroqsiz')], default='YR', max_length=2),
        ),
    ]
