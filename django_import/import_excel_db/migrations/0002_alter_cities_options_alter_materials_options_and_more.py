# Generated by Django 4.2.3 on 2023-07-29 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='surfaces',
            options={'verbose_name': 'Поверхность', 'verbose_name_plural': 'Поверхности'},
        ),
        migrations.AlterField(
            model_name='boards',
            name='latitude',
            field=models.DecimalField(decimal_places=13, max_digits=15),
        ),
        migrations.AlterField(
            model_name='boards',
            name='longitude',
            field=models.DecimalField(decimal_places=13, max_digits=15),
        ),
    ]