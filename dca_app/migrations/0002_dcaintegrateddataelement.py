# Generated by Django 3.2 on 2021-09-24 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dca_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DcaIntegratedDataElement',
            fields=[
                ('integrated_data_element_id', models.AutoField(primary_key=True, serialize=False)),
                ('integrated_data_element_version', models.IntegerField(default=1)),
                ('collection_id', models.IntegerField(blank=True, null=True)),
                ('term_id', models.IntegerField(blank=True, null=True)),
                ('integrated_data_element_lifecycle_status', models.CharField(blank=True, max_length=4000)),
                ('integrated_data_element_name', models.CharField(blank=True, max_length=4000)),
                ('commentary', models.CharField(blank=True, max_length=4000)),
                ('critical_data_element_indicator', models.CharField(blank=True, max_length=4000)),
                ('potentially_sensitive_data_element_indicator', models.CharField(blank=True, max_length=4000)),
                ('substitute_integrated_data_element_indicator', models.CharField(blank=True, max_length=4000)),
                ('last_updated_by_employee_name', models.CharField(blank=True, max_length=4000)),
                ('created_by_employee_name', models.CharField(blank=True, max_length=4000)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_updated_datetime', models.DateTimeField(auto_now=True)),
                ('integrated_data_element_version_start_date', models.DateField(blank=True, null=True)),
                ('integrated_data_element_version_end_date', models.DateField(blank=True, null=True)),
                ('key_risk_indicator', models.CharField(blank=True, max_length=4000)),
                ('integrated_dataset', models.ForeignKey(db_column='integrated_dataset_id', on_delete=django.db.models.deletion.CASCADE, related_name='id', to='dca_app.dcaintegrateddataset')),
                ('integrated_dataset_version', models.ForeignKey(db_column='integrated_dataset_version', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='integratedDatasetVersion', to='dca_app.dcaintegrateddataset')),
            ],
        ),
    ]
