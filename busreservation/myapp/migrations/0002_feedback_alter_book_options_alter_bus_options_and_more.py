# Generated by Django 5.0.3 on 2024-03-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email_Id', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'List of Books'},
        ),
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'List of Busses'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'List of Users'},
        ),
    ]
