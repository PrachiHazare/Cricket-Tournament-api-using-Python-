# Generated by Django 3.2.4 on 2021-06-17 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='rank',
        ),
        migrations.AlterField(
            model_name='matchsummary',
            name='match_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.matches'),
        ),
        migrations.AlterField(
            model_name='table',
            name='teamName',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
