# Generated by Django 4.0.4 on 2022-05-02 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_anime_user_alter_anime_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.anime')),
            ],
        ),
    ]
