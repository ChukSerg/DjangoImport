# Generated by Django 4.2.3 on 2023-07-29 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='import_excel_db.materials'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
