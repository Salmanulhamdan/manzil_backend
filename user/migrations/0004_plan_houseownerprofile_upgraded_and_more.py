# Generated by Django 4.2.6 on 2023-11-24 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_houseownerprofile_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='houseownerprofile',
            name='upgraded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='professionalsprofile',
            name='upgraded',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.plan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userplan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
