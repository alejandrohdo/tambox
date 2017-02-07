# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 14:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
        ('administracion', '0002_historicalnivelaprobacion_historicaloficina_historicalprofesion_historicalpuesto_historicaltrabajado'),
        ('requerimientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDetalleRequerimiento',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nro_detalle', models.IntegerField()),
                ('uso', models.TextField(null=True)),
                ('cantidad', models.DecimalField(decimal_places=5, max_digits=15)),
                ('cantidad_cotizada', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('cantidad_comprada', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('cantidad_atendida', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('estado', models.CharField(choices=[(b'PEND', b'PENDIENTE'), (b'COTIZ', b'COTIZADO'), (b'COTIZ_PARC', b'COTIZADO PARCIALMENTE'), (b'COMP', b'COMPRADO'), (b'COMP_PARC', b'COMPRADO PARCIALMENTE'), (b'ATEN', b'ATENDIDO'), (b'ATEN_PARC', b'ATENDIDO PARCIALMENTE'), (b'CANC', b'CANCELADO')], default=b'PEND', max_length=20)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='productos.Producto')),
                ('requerimiento', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='requerimientos.Requerimiento')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical detalle requerimiento',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRequerimiento',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('codigo', models.CharField(db_index=True, max_length=12)),
                ('motivo', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateField()),
                ('fecha_recepcion', models.DateField(null=True)),
                ('mes', models.IntegerField(choices=[(1, b'ENERO'), (2, b'FEBRERO'), (3, b'MARZO'), (4, b'ABRIL'), (5, b'MAYO'), (6, b'JUNIO'), (7, b'JULIO'), (8, b'AGOSTO'), (9, b'SETIEMBRE'), (10, b'OCTUBRE'), (11, b'NOVIEMBRE'), (12, b'DICIEMBRE')])),
                ('annio', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('observaciones', models.TextField()),
                ('informe', models.TextField(max_length=100, null=True)),
                ('entrega_directa_solicitante', models.BooleanField(default=False)),
                ('estado', models.CharField(choices=[(b'PEND', b'PENDIENTE'), (b'COTIZ', b'COTIZADO'), (b'COTIZ_PARC', b'COTIZADO PARCIALMENTE'), (b'COMP', b'COMPRADO'), (b'COMP_PARC', b'COMPRADO PARCIALMENTE'), (b'ATEN', b'ATENDIDO'), (b'ATEN_PARC', b'ATENDIDO PARCIALMENTE'), (b'CANC', b'CANCELADO')], default=b'PEND', max_length=20)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('oficina', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='administracion.Oficina')),
                ('solicitante', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='administracion.Trabajador')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical requerimiento',
            },
        ),
    ]