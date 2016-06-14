from django.db import models
# from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, UserManager
import django.utils.timezone as timezone


# Create your models here.

# save bpmn-diagram file path
def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.creator, filename)

class RFUser(models.Model):
	# link to a User model
	user = models.OneToOneField(User)
	# employ position
	position = models.CharField(max_length=128)
	def __str__(self):
		return self.user.username
	
class Project(models.Model):
	project_name = models.CharField(max_length=128, unique=True)
	creator = models.ForeignKey(
			RFUser,
			on_delete=models.CASCADE,
		)
	date_create = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.project_name
	
class Folder(models.Model):
	project_name = models.ForeignKey(
				Project,
				on_delete=models.CASCADE,
			)
	folder_id = models.IntegerField(primary_key=True, default=0)
	folder_name = models.CharField(max_length=128)
	parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.folder_name
	
# BPMN File
class BFile(models.Model):
	# print(settings.AUTH_USER_MODEL)
	creator = models.ForeignKey(
			RFUser,
			on_delete=models.CASCADE,
		)
	file_name = models.CharField(max_length=128, unique=True)
	file_save = models.FileField(upload_to=user_directory_path)
	date_create = models.DateTimeField(default=timezone.now)
	date_modify = models.DateTimeField(default=timezone.now)
	# the folder belong to
	folder = models.ForeignKey(
			Folder,
			on_delete=models.CASCADE,
		)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.file_name)
		super(BFile, self).save(*args, **kwargs)

	def __str__(self):
		return self.file_name