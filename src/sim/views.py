# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
from sim.models import Switch, Port, Link

def index(request):
    switch_list = Switch.objects.order_by('name')[:50]
    context = {'switch_list': switch_list}
    return render (request, 'sim/index.html', context)

def detail(request, switch_id):

    sw = Switch.objects.get(id=switch_id)

    result = {'id': switch_id,
         'name': sw.name,
         'description': sw.description,
         'status': "online", };

    ports = []
    for port in sw.port_set.all():
        ports.append({'name': port.name, 'is_cabled': port.is_cabled, 'is_mapped': __isMapped(switch_id, port.name)},)
    result['ports'] = ports;

    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def listMappings(request, switch_id):

    links = Link.objects.filter(Q(src_port__switch__id=switch_id) | Q(dest_port__switch__id=switch_id))
    result = []
    for l in links:
        result.append({'from': l.src_port.name, 'to': l.dest_port.name})

    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def addPorts(request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    sw = Switch.objects.get(id=switch_id)
    prefix = qd.get('prefix')
    start = qd.get('start')
    end = qd.get('end')
    for i in range(int(start), int(end) + 1):
        port_name = prefix + "." + str(i)
        if (Port.objects.filter(Q(switch=sw) & Q(name=port_name)).count() == 0):
            port = Port(switch=sw, name=port_name)
            port.save()

    return HttpResponse(simplejson.dumps({'result': "done"}, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def deletePorts(request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    prefix = qd.get('prefix')
    start = qd.get('start')
    end = qd.get('end')

    ports = Port.objects.filter(Q(switch__id=switch_id) & Q(name__startswith=prefix))
    for i in range(int(start), int(end) + 1):
        port_name = prefix + "." + str(i)
        ports.filter(name=port_name).delete()

    return HttpResponse(simplejson.dumps({'result': "done"}, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def portStatus(request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    port_name = qd.get('port')

    result = "signalDetect\n"
    if (__isMapped(switch_id, port_name)):
        result = "link\n"
    return HttpResponse(result, mimetype='application/json');

def mapPorts(request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    src_port_name = qd.get('src')
    dest_port_name = qd.get('dest')

    result = {}
    if (__isMapped(switch_id, src_port_name)):
        result['result'] = "failed"
        result['detail'] = {'reason': 'Source port is already in use'}
    elif (__isMapped(switch_id, dest_port_name)):
        result['result'] = "failed"
        result['detail'] = {'reason': 'Destination port is already in use'}
    else:
        src = Port.objects.get(Q(switch=switch_id) & Q(name=src_port_name))
        dest = Port.objects.get(Q(switch=switch_id) & Q(name=dest_port_name))
        link = Link(src_port=src, dest_port=dest)
        link.save()

        result['result'] = "done"

    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def unmapPorts(request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    src_port_name = qd.get('src')
    dest_port_name = qd.get('dest')

    src = Port.objects.get(Q(switch=switch_id) & Q(name=src_port_name))
    dest = Port.objects.get(Q(switch=switch_id) & Q(name=dest_port_name))
    link = Link.objects.filter(Q(src_port=src) & Q(dest_port=dest))

    link.delete()
    result = {'result': "done"}
    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def clearMappings (request, switch_id):
    Link.objects.filter(Q(src_port__switch__id=switch_id) | Q(dest_port__switch__id=switch_id)).delete()
    result = {'result': "done"}
    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def isMapped (request, switch_id):
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    port_name = qd.get('port')

    result = {'result': __isMapped(switch_id, port_name)}
    return HttpResponse(simplejson.dumps(result, sort_keys=True, indent=4) + "\n", mimetype='application/json');

def __isMapped(switch_id, port_name):
    linkCount = Link.objects.filter(
                                (Q(src_port__switch__id=switch_id) & Q(src_port__name=port_name)) |
                                (Q(dest_port__switch__id=switch_id) & Q(dest_port__name=port_name))
                                ).count()

    if (linkCount > 0):
        return True;
    else:
        return False;

