from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0009_alter_store_instagram_link_alter_store_snapchat_link_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Submited', 'Submited'), ('Active', 'Active'), ('Declined', 'Declined'), ('Done', 'Done')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('delivery_option', models.CharField(choices=[('Pick_Up', 'Pick Up'), ('Delivery', 'Delivery')], max_length=50)),
                ('payment_option', models.CharField(choices=[('cod', 'Cash on Delivery')], max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.store')),
            ],
        ),
    ]