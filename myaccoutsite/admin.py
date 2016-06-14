from django.contrib import admin
from myaccoutsite.models import BFile, RFUser, Project, Folder

class RFUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'position')

class FileAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('file_name', )}
	list_display = ('file_name', 'creator', 'file_save')
	
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('project_name', 'creator')
	
class FolderAdmin(admin.ModelAdmin):
	list_display = ('folder_name', 'parent_id', 'project_name')

admin.site.register(BFile, FileAdmin)
admin.site.register(RFUser, RFUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Folder, FolderAdmin)
