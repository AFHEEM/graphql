from django.contrib import admin
from .models import DcaIntegratedDataset, DcaIntegratedDataElement
# Register your models here.

admin.site.register(DcaIntegratedDataset)
admin.site.register(DcaIntegratedDataElement)