# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librokyudo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='rondas',
        ),
        migrations.RemoveField(
            model_name='ronda',
            name='flechas',
        ),
        migrations.AddField(
            model_name='flecha',
            name='ronda',
            field=models.ForeignKey(to='librokyudo.Ronda', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ronda',
            name='tirador',
            field=models.ForeignKey(to='librokyudo.Persona', default=1),
            preserve_default=False,
        ),
    ]
