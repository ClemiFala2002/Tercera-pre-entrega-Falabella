# Generated by Django 4.1.7 on 2023-03-15 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlyTrucks', '0002_post_un_campo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='heading',
            new_name='Año_de_Fabricacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='un_campo',
            new_name='Contacto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='carousel_caption_description',
            new_name='Marca_de_su_Camion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='carousel_caption_title',
            new_name='Modelo_de_su_Camion',
        ),
    ]
