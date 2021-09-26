# Generated by Django 3.2 on 2021-09-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DcaIntegratedDataset',
            fields=[
                ('integrated_dataset_id', models.AutoField(primary_key=True, serialize=False)),
                ('integrated_dataset_name', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset_version', models.IntegerField(default=1, editable=False)),
                ('dataset_confidentiality_rating', models.CharField(blank=True, max_length=4000)),
                ('dataset_person_data_classification', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset_lifecycle_status', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset_maturity_status', models.CharField(blank=True, max_length=4000)),
                ('data_steward_employee_name', models.CharField(blank=True, max_length=4000)),
                ('dataset_integrity_rating', models.CharField(blank=True, max_length=4000)),
                ('dataset_availability_rating', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset_description', models.CharField(blank=True, max_length=4000)),
                ('commentary', models.CharField(blank=True, max_length=4000)),
                ('data_user_employee_name', models.CharField(blank=True, max_length=4000)),
                ('validated_by_employee_name', models.CharField(blank=True, max_length=4000)),
                ('last_updated_by_employee_name', models.CharField(blank=True, max_length=4000)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('validated_datetime', models.DateTimeField(blank=True, null=True)),
                ('last_updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('created_by_employee_name', models.CharField(blank=True, max_length=4000)),
                ('data_user_business_line', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset_version_start_date', models.DateField(blank=True, null=True)),
                ('integrated_dataset_version_end_date', models.DateField(blank=True, null=True)),
                ('validated_by_employee_id', models.CharField(blank=True, max_length=4000)),
                ('data_user_employee_id', models.CharField(blank=True, max_length=4000)),
                ('data_steward_employee_id', models.CharField(blank=True, max_length=4000)),
                ('validated_by_employee_business_line', models.CharField(blank=True, max_length=4000)),
                ('data_steward_employee_business_line', models.CharField(blank=True, max_length=4000)),
            ],
        ),
    ]
