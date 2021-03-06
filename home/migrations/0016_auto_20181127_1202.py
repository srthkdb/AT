# Generated by Django 2.1.3 on 2018-11-27 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_discussion_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='favourite',
        ),
        migrations.AddField(
            model_name='favourite',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Discussion'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
