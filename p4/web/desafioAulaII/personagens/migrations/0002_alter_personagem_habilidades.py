# Generated by Django 5.0.2 on 2024-03-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagem',
            name='habilidades',
            field=models.TextField(),
        ),
    ]
