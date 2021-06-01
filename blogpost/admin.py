from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats
from .models import SampleModel, BlogModel, SRMModel, SRMOptionModel, WordModel, StPointModel, StPointNameModel 
# Register your models here.

class StPointNameModelResource(resources.ModelResource):
    class Meta:
        model = StPointNameModel

class StPointNameModelAdmin(ImportExportActionModelAdmin):
    ordering =['episode']
    
    list_display = (
        'episode',
        'category',
        'point'
    )

    resource_class = StPointNameModelResource
    formats = [base_formats.CSV]

admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(SRMModel)
admin.site.register(SRMOptionModel)
admin.site.register(WordModel)
admin.site.register(StPointNameModel)
admin.site.register(StPointModel)
