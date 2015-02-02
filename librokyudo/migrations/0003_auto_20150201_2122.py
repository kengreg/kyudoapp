# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librokyudo', '0002_auto_20141116_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flecha',
            name='acierto',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
