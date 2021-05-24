from django.contrib import admin
from .models import SampleModel, BlogModel, SRMModel, SRMOptionModel, WordModel, StPointModel, StPointNameModel 
# Register your models here.

admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(SRMModel)
admin.site.register(SRMOptionModel)
admin.site.register(WordModel)
admin.site.register(StPointNameModel)
admin.site.register(StPointModel)