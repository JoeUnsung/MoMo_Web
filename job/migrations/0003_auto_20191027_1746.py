# Generated by Django 2.1.5 on 2019-10-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20190728_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocationORM',
            fields=[
                ('job_location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('parent_location_id', models.IntegerField(null=True)),
                ('depth', models.SmallIntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_location',
            },
        ),
        migrations.CreateModel(
            name='JobRequireDocumentMappingORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'job_require_document_mapping',
            },
        ),
        migrations.CreateModel(
            name='JobRequireDocumentORM',
            fields=[
                ('job_require_document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'job_require_document',
            },
        ),
        migrations.AlterField(
            model_name='jobdayofweekmappingorm',
            name='day_of_week_id',
            field=models.ForeignKey(db_column='day_of_week_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobDayOfWeekORM'),
        ),
        migrations.AlterField(
            model_name='joborm',
            name='end_available_calling_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='joborm',
            name='end_working_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='joborm',
            name='start_available_calling_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='joborm',
            name='start_working_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='jobrequiredocumentmappingorm',
            name='require_document_id',
            field=models.ForeignKey(db_column='job_require_document_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.JobRequireDocumentORM'),
        ),
    ]
