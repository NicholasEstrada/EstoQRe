# Generated by Django 4.2.1 on 2023-05-17 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core0', '0003_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core0.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core0.produto')),
            ],
        ),
    ]