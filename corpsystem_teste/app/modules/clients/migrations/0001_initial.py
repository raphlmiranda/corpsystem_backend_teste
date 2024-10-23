# Generated by Django 5.0.9 on 2024-10-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'indexes': [models.Index(fields=['cpf', 'email'], name='client_unique_cpf_email_idx')],
            },
        ),
    ]
