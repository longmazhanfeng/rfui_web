from django.shortcuts import render
from django.http import HttpResponse
from myaccoutsite.models import BFile, RFUser, Folder, Project
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
		file_list = rfuser.bfile_set.all().order_by('file_name')
# 		file_list = RFUser.objects.filter(user=request.user).order_by('file_name')
		context_dict = {'files': file_list}
		return render(request, 'homepage.html', context_dict)
	else:
		return render(request, 'homepage.html')
	
def bpmnpage(request, file_name_slug):
	# get authenticated rfuser
	rfuser = RFUser.objects.filter(user=request.user)[0]
	# get chosen file	
	file = rfuser.bfile_set.all().filter(slug=file_name_slug)[0]
	file_save = file.file_save
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

def savejson(request, file_name_slug):
	if request.is_ajax():
		if request.method == 'POST':
			# decode bytes http data to json format
			json_data = json.loads(request.body.decode('utf-8'))
			# pprint(json_data)
			# print(json_data['xml'])
			
			# get authenticated rfuser
			rfuser = RFUser.objects.filter(user=request.user)[0]
			# get chosen file	
			file = rfuser.bfile_set.all().filter(slug=file_name_slug)[0]
			file_save = file.file_save
			# utf-8 file write
			file_bpmn = codecs.open(file_save.path, 'w', 'utf-8')
			try:
				# write xml data to file
				file_bpmn.write(json_data['xml'])
			finally:
				file_bpmn.close()
	return HttpResponse("OK")

def testpage(request):
	folders = Folder.objects.all()
	for folder in folders:
		if folder.parent_id == None:
			tree_root = folder
			break
# 	print(json.dumps(get_folder(tree_root)))
	return render(request, 'pm_homepage.html', {'tree_json': json.dumps(get_folder(tree_root))})

# use recurion get jstree tree-format json data from database 
def get_folder(folder):
	root = {}
	root['id'] = folder.folder_id
	root['text'] = folder.folder_name
	children = Folder.objects.filter(parent_id=folder.folder_id)
	if children:
		root_children = []
		for child in children:
			root_children.append(get_folder(child))
		root['children'] = root_children
	return root
		
			