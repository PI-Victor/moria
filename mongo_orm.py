#import mongoengine
from mongoengine import *

connect('kpis')


class Kpis(Document):
    

