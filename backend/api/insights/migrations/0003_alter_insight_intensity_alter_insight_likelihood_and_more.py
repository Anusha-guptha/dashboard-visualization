# Generated by Django 5.1.1 on 2024-10-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_alter_insight_pestle_alter_insight_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='intensity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='insight',
            name='likelihood',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='insight',
            name='relevance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='insight',
            name='source',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='insight',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
