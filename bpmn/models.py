from django.db import models
from django.template.defaultfilters import default
from django.utils import timezone

# Create your models here.
class BpmnProject(models.Model):
    project_name = models.CharField(max_length=128, unique=True)
    file_save = models.FileField(upload_to="bpmn_files/")
    date_create = models.DateTimeField('创建日期', default = timezone.now())
    date_modify = models.DateTimeField('最后修改日期', auto_now = True)

    def __str__(self):
        return self.project_name