# Generated by Django 3.2.7 on 2021-09-25 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_auto_20210925_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]
