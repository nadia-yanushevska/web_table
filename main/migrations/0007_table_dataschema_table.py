# Generated by Django 4.1.7 on 2023-03-16 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_dataschema_name_remove_dataschema_x_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null='True')),
            ],
        ),
        migrations.AddField(
            model_name='dataschema',
            name='table',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='main.table'),
            preserve_default='True',
        ),
    ]
