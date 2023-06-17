# Generated by Django 4.2.2 on 2023-06-17 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0007_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='images/placeholder.png', upload_to='images/')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.store')),
            ],
        ),
    ]