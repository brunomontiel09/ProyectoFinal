# Generated by Django 4.1.5 on 2023-02-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPeliseries', '0005_alter_musica_autor_alter_pelicula_autor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='fechaestreno',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='genero2',
        ),
        migrations.AddField(
            model_name='serie',
            name='añoestreno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='serie',
            name='cantepisodios',
            field=models.IntegerField(default=1),
        ),
    ]
