from mongoengine import *  
import datetime


try:
    connect('kpidb')
except ConnectionError as e:
    exit('Connection to mongo refused')


class Kpis(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    cpu_softirq = FloatField()
    cpu_iowait = FloatField()
    cpu_sys = FloatField()
    cpu_gues = FloatField()
    cpu_idle = FloatField()
    cpu_user = FloatField()
    cpu_guestnice = FloatField()
    cpu_irq = FloatField()
    cpu_steal = FloatField()
    cpu_nice = FloatField()
    
