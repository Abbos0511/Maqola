# Generated by Django 3.2.9 on 2021-11-23 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('tags', models.CharField(max_length=400)),
                ('published_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkedFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=500, null=True)),
                ('faculty', models.CharField(max_length=200, null=True)),
                ('chair', models.CharField(max_length=220, null=True)),
                ('image', models.ImageField(default='', upload_to='')),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor'),
        ),
    ]