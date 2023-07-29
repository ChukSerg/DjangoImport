# Generated by Django 4.2.3 on 2023-07-29 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0003_boards_code_surface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='surface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='import_excel_db.surfaces'),
        ),
        migrations.AlterUniqueTogether(
            name='boards',
            unique_together={('in_code', 'surface')},
        ),
    ]
