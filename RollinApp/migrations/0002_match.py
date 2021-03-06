# Generated by Django 3.2.6 on 2021-09-03 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RollinApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchType', models.CharField(blank=True, choices=[('Group Stage', 'Group Stage'), ('Play Offs', 'Play Offs')], max_length=50, null=True)),
                ('team1', models.CharField(blank=True, max_length=50, null=True)),
                ('team2', models.CharField(blank=True, max_length=50, null=True)),
                ('victory', models.CharField(blank=True, max_length=50, null=True)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RollinApp.tournament')),
            ],
        ),
    ]
