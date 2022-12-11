# Generated by Django 2.2.14 on 2022-12-11 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_auto_20221211_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
                ('payment_date', models.DateTimeField(default=None, null=True)),
                ('examination_date', models.DateTimeField()),
                ('address', models.CharField(max_length=500)),
                ('total', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]