# Generated by Django 3.2.4 on 2021-06-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_stripemodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
