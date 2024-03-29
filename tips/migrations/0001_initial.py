# Generated by Django 3.2.5 on 2021-07-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.TextField(null=True)),
                ('poster', models.CharField(max_length=50)),
                ('poster_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
