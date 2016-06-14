from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from bpmn import views


urlpatterns = [
    url(r"^editpage/$", views.create_bpmn, name="create_bpmn"),
    url(r"^editpage/(?P<project_str>\w{6})/$", views.bpmn_editpage, name="editpage"),
    url(r"^editpage/(?P<project_str>\w{6})/savejson/$", views.savebpmn, name="savejson"),
#     url(r"^admin/", include(admin.site.urls)),
#     url(r"^account/", include("account.urls")),
#     url(r"^details/(?P<project_name_slug>[\w\-]+)/$", views.bpmnpage, name="details_bpms"),
#     url(r"^details/(?P<project_name_slug>[\w\-]+)/savejson/", views.savejson, name="savejson"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
