# Generated by Django 5.0.1 on 2024-02-04 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_balance_after_borrow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]
