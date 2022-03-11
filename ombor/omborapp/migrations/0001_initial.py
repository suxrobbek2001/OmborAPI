# Generated by Django 3.2.12 on 2022-03-10 04:10

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
            name='Ombor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('dokon_nomi', models.CharField(max_length=30)),
                ('joylashuv', models.CharField(max_length=30)),
                ('turi', models.CharField(blank=True, max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('brend_nomi', models.CharField(blank=True, max_length=30)),
                ('narx', models.IntegerField()),
                ('miqdor', models.IntegerField()),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='omborapp.ombor')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('dokon_nomi', models.CharField(max_length=30)),
                ('joylashuv', models.CharField(max_length=30)),
                ('qarz', models.IntegerField(default=0)),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='omborapp.ombor')),
            ],
        ),
    ]
