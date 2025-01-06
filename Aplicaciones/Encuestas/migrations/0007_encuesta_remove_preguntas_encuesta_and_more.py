# Generated by Django 5.1.3 on 2025-01-04 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encuestas', '0006_encuestas_remove_pregunta_titulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='encuesta',
        ),
        migrations.RemoveField(
            model_name='respuestas',
            name='pregunta',
        ),
        migrations.AlterField(
            model_name='respuestausuario',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Encuestas.encuesta'),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='Encuestas.encuesta')),
            ],
        ),
        migrations.AlterField(
            model_name='respuestausuario',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Encuestas.pregunta'),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='Encuestas.pregunta')),
            ],
        ),
        migrations.AlterField(
            model_name='respuestausuario',
            name='respuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Encuestas.respuesta'),
        ),
        migrations.DeleteModel(
            name='Encuestas',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
        migrations.DeleteModel(
            name='Respuestas',
        ),
    ]