from django.contrib import admin
from myaccoutsite.models import Project, RFUser

class RFUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'position')

class ProjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('project_name', )}
	list_display = ('project_name', 'creator', 'file_save')

admin.site.register(Project, ProjectAdmin)
admin.site.register(RFUser, RFUserAdmin)