# Generated by Django 5.0.1 on 2024-02-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_user_bookreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='review',
            field=models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5')], max_length=10),
        ),
    ]