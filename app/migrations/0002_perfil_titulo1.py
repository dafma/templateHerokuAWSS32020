# Generated by Django 3.0.5 on 2020-05-02 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='titulo1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
