# Generated by Django 5.0.1 on 2024-02-04 02:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='book/media/images/')),
                ('description', models.TextField()),
                ('borrowed_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('balance_after_borrow', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categories', models.ManyToManyField(to='category.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['borrowed_date'],
            },
        ),
    ]
