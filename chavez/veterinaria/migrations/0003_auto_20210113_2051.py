# Generated by Django 3.1.5 on 2021-01-14 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0002_mascota_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='apellidos')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('telefono', models.CharField(max_length=500, verbose_name='telefono')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(verbose_name='descrpcion')),
            ],
            options={
                'verbose_name': 'veterinario',
                'verbose_name_plural': 'veterinarios',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horainicio', models.CharField(max_length=50, verbose_name='horainicio')),
                ('horafin', models.CharField(max_length=50, verbose_name='horafin')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.doctor')),
            ],
            options={
                'verbose_name': 'horario',
                'verbose_name_plural': 'horarios',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='reservacita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=10, verbose_name='fecha')),
                ('inicio', models.CharField(max_length=60, verbose_name='inicio')),
                ('fin', models.CharField(max_length=60, verbose_name='fin')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.horario')),
            ],
            options={
                'verbose_name': 'cita',
                'verbose_name_plural': 'citas',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='tipocita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tipocita',
                'verbose_name_plural': 'tipocitas',
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterModelOptions(
            name='controlv',
            options={'ordering': ['created_on'], 'verbose_name': 'controlv', 'verbose_name_plural': 'controlv'},
        ),
        migrations.AlterModelOptions(
            name='tipov',
            options={'ordering': ['created_on'], 'verbose_name': 'tipoV', 'verbose_name_plural': 'tipoVs'},
        ),
        migrations.RemoveField(
            model_name='historia',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='historia',
            name='motivo',
        ),
        migrations.AlterField(
            model_name='controlv',
            name='observacion',
            field=models.TextField(verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='historia',
            name='observaciones',
            field=models.TextField(verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='carnet',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='carnet'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='especie',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='observaciones',
            field=models.TextField(verbose_name='observaciones'),
        ),
        migrations.AlterField(
            model_name='tipov',
            name='descripcion',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.DeleteModel(
            name='cita',
        ),
        migrations.AddField(
            model_name='reservacita',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.mascota'),
        ),
        migrations.AddField(
            model_name='reservacita',
            name='tipocita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.tipocita'),
        ),
    ]
