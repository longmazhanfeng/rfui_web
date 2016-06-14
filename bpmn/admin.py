from django.contrib import admin
from bpmn.models import BpmnProject

# Register your models here.
class BpmnProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'file_save')
    
admin.site.register(BpmnProject, BpmnProjectAdmin)