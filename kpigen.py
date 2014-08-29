import time
import random

#Author: p-victor @ palade.ionut@gmail.com
#The codeflavour Org

"""Generate random KPIs with randon values,
must have a way to tweak the value to high or low for
better simulation and it should be time dependent so
it can simulate traffic KPIs in a telecom core network
"""

charlist = 'AbCDeFgHijklmnopQrStuVwxyZ231_654987-'
multiplier = 10 # use the multiplier to increase/decrease the kpi value
hashno = 10 # number of KPIs a time series event should have
time_event = {} #the hash itself
sleep_timer = 60 * 5  # generate every 60 * n
kpi_len = 5

kpi_types = {1: 'int',
            2: 'string',
            3: 'boolean',
            4: 'float'}


def gen_kpi():
    """generate a random kpi name with the specified length
    add the random kpi to the hash
    """
    kpi_name = ''
    for i in range(kpi_len):
        kpi_name = kpi_name + charlist[random.randrange(len(charlist))]
    return kpi_name

def gen_value():
    kpi_gender = kpi_types[random.randrange(1,4)]
    if kpi_gender == 'string':
        service_stat = ['running','faulted', 'offline']
        value_type = service_stat[random.randrange(1,3)]
    elif kpi_gender == 'int':
        value_type = random.randrage(0,100)
    elif kpi_gender == 'boolean':
        bool_stat = ['False','True']
        value_type = bool_stat[random.randrange(2)]
    elif kpi_gender == 'float':
        value_type = random.randrange(1,100) / 2.5
    else:
        return 
    return value_type

def gen_def():
    """generate a kpi definition """
    kpi_gender = gen_value()   # yeah i know i ran out of names
    print kpi_gender
    pass
    for i in range(1,5):
        kpi_types
    return 

def inject_kpi():
    for i in range(hashno):
        kpi_name = generate_kpis()
        
        time_event.setdefault(kpi_name, 1                         
                       )

def main():
    gen_def()

if __name__ == '__main__':
    main()
