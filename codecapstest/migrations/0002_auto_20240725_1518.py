# Generated by Django 2.2.22 on 2024-07-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codecapstest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testField', models.CharField(max_length=10000)),
                ('testField2', models.TextField()),
                ('testField3', models.BinaryField(editable=True)),
            ],
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='testField2',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=20),
        ),
    ]
