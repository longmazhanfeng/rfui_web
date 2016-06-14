from django.shortcuts import render
from django.shortcuts import redirect
from bpmn.models import BpmnProject
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse

import json
from pprint import pprint
import random, string
import tempfile
import os

# local bpmnfile path
bpmnfile_path = settings.MEDIA_ROOT + '/bpmn_files'

# newDiagramXML content which will be writed to a new empty bpmn file
newDiagramXML = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<bpmn2:definitions xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:bpmn2=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:dc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:di=\"http://www.omg.org/spec/DD/20100524/DI\" xsi:schemaLocation=\"http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd\" id=\"sample-diagram\" targetNamespace=\"http://bpmn.io/schema/bpmn\">\n  <bpmn2:process id=\"Process_1\" isExecutable=\"false\">\n    <bpmn2:startEvent id=\"StartEvent_1\"/>\n  </bpmn2:process>\n  <bpmndi:BPMNDiagram id=\"BPMNDiagram_1\">\n    <bpmndi:BPMNPlane id=\"BPMNPlane_1\" bpmnElement=\"Process_1\">\n      <bpmndi:BPMNShape id=\"_BPMNShape_StartEvent_2\" bpmnElement=\"StartEvent_1\">\n        <dc:Bounds height=\"36.0\" width=\"36.0\" x=\"412.0\" y=\"240.0\"/>\n      </bpmndi:BPMNShape>\n    </bpmndi:BPMNPlane>\n  </bpmndi:BPMNDiagram>\n</bpmn2:definitions>"

# error message
error_msg = {'MaxError': '服务器数据爆满，无法创建新文件，请联系hzdonghao@corp.netease.com'}

# create a new bpmn file
def create_bpmn(request):
    # generate a random 6-bit string 
    project_str = ''.join(random.sample(string.ascii_letters+string.digits, 6)) + '/'
    return redirect(project_str)

def bpmn_editpage(request, project_str):
    ls = BpmnProject.objects.filter(project_name=project_str)
    # if p is none, create a new bpmn file   
    if len(ls) == 0:
#       create a new bpmn project
        p = BpmnProject(project_name=project_str)   
        p.save()    
#         pprint(p)   
        # if the number of local files is out of 500, throw a error message 
        if len(os.listdir(bpmnfile_path)) > 500:
            return render(request, 'editpage.html', {'Dict': json.dumps(error_msg)})

        # use tempfile which will be automatically cleaned up
        temp = tempfile.TemporaryFile(mode='w+t')
        temp.write(newDiagramXML)
        p.file_save.save(project_str, File(temp))
        temp.close() 
           
    p = BpmnProject.objects.filter(project_name=project_str)[0]  
    # read a bpmn file which was existed or created before    
    file_save = p.file_save
    file_bpmn = open(file_save.path, 'r')
    try:
        bpmn_xml = file_bpmn.read()
        context_dict = {'bpmn_xml': bpmn_xml}
    finally:
        file_bpmn.close()    
    
    # process the dict data
    return render(request, 'editpage.html', {'Dict': json.dumps(context_dict)})

def savebpmn(request, project_str):
    if request.is_ajax():
        if request.method == 'POST':
            # decode bytes http data to json format
            json_data = json.loads(request.body.decode('utf-8'))
            
            # get chosen project    
            project = BpmnProject.objects.filter(project_name=project_str)[0]
            file_save = project.file_save
            # utf-8 file write
            # file_bpmn = codecs.open(file_save.path, 'w', 'utf-8')
            file_bpmn = open(file_save.path, 'w')
            try:
                # write xml data to file
                file_bpmn.write(json_data['xml'])
            finally:
                file_bpmn.close()
    return HttpResponse("OK")