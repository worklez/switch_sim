from django.conf.urls import patterns, url
from sim import views

urlpatterns = patterns('',
                       # ex:  /sim/
                       url(r'^$', views.index, name="index"),

                       # ex:  /sim/5/
                       url(r'^(?P<switch_id>\d+)/$', views.detail, name='detail'),

                       # ex: /sim/5/listMappings/
                       url(r'^(?P<switch_id>\d+)/listMappings', views.listMappings, name='listMappings'),

                       # ex: /sim/5/addPorts
                       url(r'^(?P<switch_id>\d+)/addPorts', views.addPorts, name="addPorts"),

                       # ex: /sim/5/deletePorts
                       url(r'^(?P<switch_id>\d+)/deletePorts', views.deletePorts, name="deletePorts"),

                       # ex: /sim/5/portStatus
                       url(r'^(?P<switch_id>\d+)/portStatus', views.portStatus, name="portStatus"),

                       # ex: /sim/5/map/
                       url(r'^(?P<switch_id>\d+)/map', views.mapPorts, name="mapPorts"),

                       # ex: /sim/5/unmap/
                       url(r'^(?P<switch_id>\d+)/unmap', views.unmapPorts, name="unmapPorts"),

                       # ex: /sim/5/clearMapping/
                       url(r'^(?P<switch_id>\d+)/clearMappings', views.clearMappings, name="clearMappings"),

                       # ex: /sim/5/isMapped/
                       url(r'^(?P<switch_id>\d+)/isMapped', views.isMapped, name="isMapped"),
                       )

