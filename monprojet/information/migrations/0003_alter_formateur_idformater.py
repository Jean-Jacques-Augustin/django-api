# Generated by Django 5.0 on 2023-12-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_module_idmodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formateur',
            name='IdFormater',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]