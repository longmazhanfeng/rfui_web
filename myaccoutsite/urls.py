from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from myaccoutsite import views


urlpatterns = [
#     url(r"^$", views.homepage, name="home"),
    url(r"^$", views.testpage, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    # bpmn app urls 
    url(r"^bpmn/", include("bpmn.urls")),
    url(r"^details/(?P<file_name_slug>[\w\-]+)/$", views.bpmnpage, name="details_bpms"),
    url(r"^details/(?P<file_name_slug>[\w\-]+)/savejson/", views.savejson, name="savejson"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
