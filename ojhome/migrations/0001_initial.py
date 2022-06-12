# Generated by Django 4.0.5 on 2022-06-12 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('createdOn', models.DateTimeField(verbose_name='created on')),
                ('testcase', models.FileField(upload_to='testcases/%Y/%m/%d/')),
                ('answer', models.FileField(upload_to='answers/%Y/%m/%d/')),
                ('title', models.CharField(default='', max_length=50)),
                ('level', models.CharField(max_length=6)),
                ('timeout', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('registeredOn', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=100)),
                ('verdictCode', models.IntegerField(default=0)),
                ('submittedOn', models.DateTimeField(verbose_name='time submitted')),
                ('code', models.TextField(default='')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojhome.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojhome.user')),
            ],
        ),
    ]
