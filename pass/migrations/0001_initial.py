# Generated by Django 4.2.5 on 2023-09-16 15:23

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('category', models.CharField(choices=[('Sanitary Measures, Food & Shelter', 'Sanitary Measures, Food & Shelter'), ('Art, Cultural & Arrchitectural Conservation', 'Art, Cultural & Arrchitectural Conservation'), ('Creativity & Empowerment', 'Creativity & Empowerment')], max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 300], upload_to='media')),
                ('image2', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 300], upload_to='media')),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[400, 300], upload_to='media')),
                ('initial_price', models.PositiveIntegerField()),
                ('target_price', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=70)),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, scale=None, size=[200, 100], upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass.member')),
            ],
        ),
    ]
