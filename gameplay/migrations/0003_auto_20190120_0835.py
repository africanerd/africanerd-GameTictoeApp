# Generated by Django 2.1.4 on 2019-01-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_auto_20190114_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
