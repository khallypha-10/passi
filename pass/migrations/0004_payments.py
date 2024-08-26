# Generated by Django 4.2.5 on 2024-08-26 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0003_alter_member_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('amount', models.PositiveIntegerField()),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cause', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pass.cause')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
