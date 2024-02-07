# Generated by Django 5.0.1 on 2024-02-04 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_useraccount_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_after_borrowed', models.DecimalField(decimal_places=2, max_digits=12)),
                ('on_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount')),
            ],
            options={
                'ordering': ['on_date'],
            },
        ),
    ]