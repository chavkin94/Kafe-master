# Generated by Django 3.1.7 on 2021-04-29 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lapa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='tip_tovara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tovari_set', to='lapa.tiptovara', verbose_name='Тип товара'),
        ),
    ]