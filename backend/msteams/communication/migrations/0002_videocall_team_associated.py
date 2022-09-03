# Generated by Django 3.2.4 on 2021-06-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_teams_admin'),
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocall',
            name='team_associated',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teams.teams'),
            preserve_default=False,
        ),
    ]