# Generated by Django 4.0.4 on 2022-06-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0013_alter_post_cloth_type_alter_post_washtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='drycleaning',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='repair',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=20),
        ),
    ]
