# Generated by Django 4.0.3 on 2023-07-02 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('documents', models.ManyToManyField(to='schoolapp.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.newuser'),
        ),
    ]
