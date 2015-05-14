from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^main/addList$', 'agenda.views.add_list'),
    url(r'^main/(?P<list_name>\w+)$', 'agenda.views.each'),
    url(r'^main/(?P<task_name>\w+)/remove$', 'agenda.views.remove'),
    url(r'^main/(?P<list_name>\w+)/addTask$', 'agenda.views.add_task'),
    url(r'^main/(?P<list_name>\w+)/doit$', 'agenda.views.doer'),
    url(r'^done$', 'agenda.views.done'),
    url(r'^main/$', 'agenda.views.main'),
    url(r'^admin/', include(admin.site.urls)),
]
