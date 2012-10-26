from django.contrib import admin
from sim.models import Switch, Port, Link

class PortInline (admin.TabularInline):
    model = Port
    extra = 3

class SwitchAdmin (admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [PortInline]
    list_display = ('name', 'description', 'port_count')

class LinkAdmin (admin.ModelAdmin):
    list_display = ('src_switch', 'src_port_name', 'dest_switch', 'dest_port_name')
    
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Link, LinkAdmin)
