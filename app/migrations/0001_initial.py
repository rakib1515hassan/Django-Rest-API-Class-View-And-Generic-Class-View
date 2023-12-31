# Generated by Django 4.2.2 on 2023-06-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_class', models.CharField(choices=[('vi', 'vi'), ('vii', 'vii'), ('viii', 'viii'), ('ix', 'ix'), ('x', 'x')], default='vi', max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('roll', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='Profile')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('waiver', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('salary', models.IntegerField()),
                ('experience', models.BooleanField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
