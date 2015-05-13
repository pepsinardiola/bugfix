from django.conf.urls import include, url
from django.contrib import admin
from agenda import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'sina.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/$', 'agenda.views.main'),
    url(r'^main/(?P<list_name>\w+)$', 'agenda.views.each'),
    url(r'^main/done$', 'agenda.views.done'),
    url(r'^main/remove/(?P<task_name>\w+)$', 'agenda.views.remove'),
    url(r'^main/addTask/(?P<list_name>\w+)$', 'agenda.views.add_task'),
    url(r'^main/addList/$', 'agenda.views.add_list'),
    url(r'^main/doit/(?P<list_name>\w+)$', 'agenda.views.doer'),
    url(r'^admin/', include(admin.site.urls)),
]
