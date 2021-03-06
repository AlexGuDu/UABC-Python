# Generated by Django 2.1 on 2018-12-06 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complain_o_citizen_2000', '0002_bigcomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='empty')),
                ('bigcomplaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain_o_citizen_2000.BigComplaint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain_o_citizen_2000.User')),
            ],
        ),
    ]
