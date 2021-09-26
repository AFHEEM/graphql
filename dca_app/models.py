# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DcaIntegratedDataset(models.Model):
    integrated_dataset_id = models.AutoField(primary_key=True)
    integrated_dataset_name = models.CharField(max_length=4000)
    integrated_dataset_version = models.IntegerField(default=1, editable=False)
    dataset_confidentiality_rating = models.CharField(max_length=4000)
    dataset_person_data_classification = models.CharField(max_length=4000)
    integrated_dataset_lifecycle_status = models.CharField(max_length=4000)
    integrated_dataset_maturity_status = models.CharField(max_length=4000)
    data_steward_employee_name = models.CharField(max_length=4000)
    dataset_integrity_rating = models.CharField(max_length=4000)
    dataset_availability_rating = models.CharField(max_length=4000)
    integrated_dataset_description = models.CharField(max_length=4000)
    commentary = models.CharField(max_length=4000)
    data_user_employee_name = models.CharField(max_length=4000)
    validated_by_employee_name = models.CharField(max_length=4000)
    last_updated_by_employee_name = models.CharField(max_length=4000)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    validated_datetime = models.DateTimeField(blank=True, null=True)
    last_updated_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by_employee_name = models.CharField(max_length=4000)
    data_user_business_line = models.CharField(max_length=4000)
    integrated_dataset_version_start_date = models.DateField(blank=True, null=True)
    integrated_dataset_version_end_date = models.DateField(blank=True, null=True)
    validated_by_employee_id = models.CharField(max_length=4000)
    data_user_employee_id = models.CharField(max_length=4000)
    data_steward_employee_id = models.CharField(max_length=4000)
    validated_by_employee_business_line = models.CharField(max_length=4000)
    data_steward_employee_business_line = models.CharField(max_length=4000)

    def save(self, *args, **kwargs):
        super(DcaIntegratedDataset, self).save(*args, **kwargs)
        if not self.integrated_dataset_name:
            self.integrated_dataset_name = "IDS_NAME_" + str(self.integrated_dataset_id)
            super(DcaIntegratedDataset, self).save(update_fields=['integrated_dataset_name'])

    def __str__(self):
        return self.integrated_dataset_name


class DcaIntegratedDataElement(models.Model):
    integrated_data_element_id = models.AutoField(primary_key=True)
    integrated_data_element_version = models.IntegerField(default=1, editable=True)
    integrated_dataset = models.ForeignKey('DcaIntegratedDataset', on_delete=models.CASCADE,
                                           db_column='integrated_dataset_id', related_name='id')
    integrated_dataset_version = models.ForeignKey('DcaIntegratedDataset', models.DO_NOTHING,
                                                   db_column='integrated_dataset_version',
                                                   related_name='integratedDatasetVersion', default=1, editable=True)
    collection_id = models.IntegerField(blank=True, null=True)
    term_id = models.IntegerField(blank=True, null=True)
    integrated_data_element_lifecycle_status = models.CharField(max_length=4000)
    integrated_data_element_name = models.CharField(max_length=4000)
    commentary = models.CharField(max_length=4000)
    critical_data_element_indicator = models.CharField(max_length=4000)
    potentially_sensitive_data_element_indicator = models.CharField(max_length=4000)
    substitute_integrated_data_element_indicator = models.CharField(max_length=4000)
    last_updated_by_employee_name = models.CharField(max_length=4000)
    created_by_employee_name = models.CharField(max_length=4000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    last_updated_datetime = models.DateTimeField(auto_now=True)
    integrated_data_element_version_start_date = models.DateField(blank=True, null=True)
    integrated_data_element_version_end_date = models.DateField(blank=True, null=True)
    key_risk_indicator = models.CharField(max_length=4000)

    def save(self, *args, **kwargs):
        super(DcaIntegratedDataElement, self).save(*args, **kwargs)
        if not self.integrated_data_element_name:
            self.integrated_data_element_name = "IDE_NAME_" + str(self.integrated_data_element_id)
            super(DcaIntegratedDataElement, self).save(update_fields=['integrated_data_element_name'])

    def __str__(self):
        return self.integrated_data_element_name
