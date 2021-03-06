from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from .models import SampleModel, BlogModel, SRMModel, SRMOptionModel, WordModel, StPointModel, MonitorModel, ExerciseModel, StPointNameModel
# Register your models here.

class StPointNameModelResource(resources.ModelResource):
    class Meta:
        model = StPointNameModel

class StPointModelResource(resources.ModelResource):
    class Meta:
        model = StPointModel
        import_id_fields = ['point_date']

class SRMModelResource(resources.ModelResource):
    class Meta:
        model = SRMModel
        import_id_fields = ['SRM_date']

class SRMOptionModelResource(resources.ModelResource):
    class Meta:
        model = SRMOptionModel

class WordModelResource(resources.ModelResource):
    class Meta:
        model = WordModel

class MonitorModelResource(resources.ModelResource):
    class Meta:
        model = MonitorModel

class ExerciseModelResource(resources.ModelResource):
    class Meta:
        model = ExerciseModel

admin.site.register(SampleModel)
admin.site.register(BlogModel)

@admin.register(StPointNameModel)
class StPointNameModelAdmin(ImportExportModelAdmin):
    ordering =['id']
    
    resource_class = StPointNameModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("04_St_name",
                              file_format.get_extension())
        return filename    
        
@admin.register(StPointModel)
class StPointModelAdmin(ImportExportModelAdmin):
    ordering =['-point_date']

    resource_class = StPointModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("03_St_point",
                              file_format.get_extension())
        return filename    
        
@admin.register(SRMModel)
class SRMModelAdmin(ImportExportModelAdmin):
    ordering =['-SRM_date']

    resource_class = SRMModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("01_SRM",
                              file_format.get_extension())
        return filename    
        
@admin.register(SRMOptionModel)
class SRMOptionModelAdmin(ImportExportModelAdmin):
    resource_class = SRMOptionModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("02_SRMOP",
                              file_format.get_extension())
        return filename    
        
@admin.register(WordModel)
class WordModelAdmin(ImportExportModelAdmin):
    resource_class = WordModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("07_Word",
                              file_format.get_extension())
        return filename    
        
@admin.register(MonitorModel)
class MonitorModelAdmin(ImportExportModelAdmin):
    resource_class = MonitorModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("05_monitor",
                              file_format.get_extension())
        return filename    

@admin.register(ExerciseModel)
class ExerciseModelAdmin(ImportExportModelAdmin):
    resource_class = ExerciseModelResource
    formats = [base_formats.CSV]

    def get_export_filename(self, request, queryset, file_format):
        filename = "%s.%s" % ("06_exercise",
                              file_format.get_extension())
        return filename    
