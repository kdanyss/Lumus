# Generated by Django 4.0.3 on 2022-06-05 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumus', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('Mostrar', 'Mostrar'), ('Não Mostrar', 'Não Mostrar')], default='Permitido', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Mostrar', 'Mostrar'), ('Não Mostrar', 'Não mostrar')], default='Permitido', max_length=15),
        ),
    ]
