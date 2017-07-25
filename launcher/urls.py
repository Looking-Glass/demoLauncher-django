from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from launcher import views as launcherViews
from computer import views as computerViews
admin.autodiscover()

urlpatterns = [
    url(r'^$', launcherViews.home, name='home'),
    url(r'^computer/(?P<computerName>[\w-]+)/', launcherViews.computer, name='computer'),
    url(r'^update/', computerViews.update, name='update'),    
    url(r'^action/', launcherViews.action, name='action'),    
    url(r'^admin/', include(admin.site.urls)),
]

