from django.db import models

# Create your models here.
class Switch(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.name
    
    def port_count (self):
        return self.port_set.count()
    port_count.short_description = 'Num of Ports'
    
class Port(models.Model):
    switch = models.ForeignKey(Switch)
    name = models.CharField(max_length=20)
    is_cabled = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.switch.__str__() + ':' + self.name)

class Link(models.Model):
    src_port = models.ForeignKey(Port, related_name="src_port")
    dest_port = models.ForeignKey(Port, related_name="dest_port")
    
    def __unicode__(self):
        return (self.src_port.__str__() + "==" + self.dest_port.__str__())
    
    def src_switch (self):
        return self.src_port.switch
    
    def dest_switch (self):
        return self.dest_port.switch

    def src_port_name (self):
        return self.src_port.name
    
    def dest_port_name (self):
        return self.dest_port.name
    
    src_switch.admin_order_field = 'src_port'
    dest_switch.admin_order_field = 'dest_port'