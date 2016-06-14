from django.shortcuts import render
from django.http import HttpResponse
from myaccoutsite.models import Project, RFUser
# process utf-8 file
import codecs
import json
from pprint import pprint
# Create your views here.

def homepage(request):
	if request.user.is_authenticated():
		# get authenticated rfuser
		rfuser = RFUser.objects.filter(user=request.user)[0]
		# show info of current user
		project_list = rfuser.project_set.all().order_by('project_name')
# 		project_list = RFUser.objects.filter(user=request.user).order_by('project_name')
		context_dict = {'projects': project_list}
		return render(request, 'homepage.html', context_dict)
	else:
		return render(request, 'homepage.html')
	
def bpmnpage(request, project_name_slug):
	# get authenticated rfuser
	rfuser = RFUser.objects.filter(user=request.user)[0]
	# get chosen project	
	project = rfuser.project_set.all().filter(slug=project_name_slug)[0]
	file_save = project.file_save
	# utf-8 file read
	file_bpmn = codecs.open(file_save.path, 'r', 'utf-8')
	try:
		bpmn_xml = file_bpmn.read()
		context_dict = {'bpmn_xml': bpmn_xml}
		# print(bpmn_xml)
	finally:
		file_bpmn.close()	
	
	# process the dict data
	return render(request, 'bpmnpage.html', {'Dict': json.dumps(context_dict)})

def savejson(request, project_name_slug):
	if request.is_ajax():
		if request.method == 'POST':
			# decode bytes http data to json format
			json_data = json.loads(request.body.decode('utf-8'))
			# pprint(json_data)
			# print(json_data['xml'])
			
			# get authenticated rfuser
			rfuser = RFUser.objects.filter(user=request.user)[0]
			# get chosen project	
			project = rfuser.project_set.all().filter(slug=project_name_slug)[0]
			file_save = project.file_save
			# utf-8 file write
			file_bpmn = codecs.open(file_save.path, 'w', 'utf-8')
			try:
				# write xml data to file
				file_bpmn.write(json_data['xml'])
			finally:
				file_bpmn.close()
	return HttpResponse("OK")