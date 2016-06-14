from django.db import models
# from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, UserManager
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
	# print(settings.AUTH_USER_MODEL)
	creator = models.ForeignKey(
			RFUser,
			on_delete=models.CASCADE,
		)
	project_name = models.CharField(max_length=128, unique=True)
	file_save = models.FileField(upload_to=user_directory_path)
	date_create = models.DateTimeField()
	date_modify = models.DateTimeField()
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.project_name)
		super(Project, self).save(*args, **kwargs)

	def __str__(self):
		return self.project_name