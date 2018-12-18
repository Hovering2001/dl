if __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from core.log import *

def test(classname, conf, verbose):
    classname(conf=conf).run(310)
    if verbose:
        logcat()
    sum_dmg()
    return



def sum_dmg():
    l = logget()
    dmg_sum = {'x': [0, 0], 's': 0  }
    sdmg_sum = {'s1':[0, 0], 's2':[0, 0], 's3':[0, 0]}
    xdmg_sum = {"x1":0, "x2":0, "x3":0, "x4":0, "x5":0 }
    for i in l:
        if i[1] == 'dmg':
            #dmg_sum[i[2][0]] += i[3]
            if i[2][0] == 'x':
                dmg_sum['x'][0] += i[3]
            elif i[2] == 's1':
                dmg_sum['s'] += i[3]
                sdmg_sum['s1'][0] += i[3]
            elif i[2] == 's2':
                dmg_sum['s'] += i[3]
                sdmg_sum['s2'][0] += i[3]
            elif i[2] == 's3':
                dmg_sum['s'] += i[3]
                sdmg_sum['s3'][0] += i[3]
        elif i[1] == 'cast':
            if i[2] == 's1':
                sdmg_sum['s1'][1] += 1
            elif i[2] == 's2':
                sdmg_sum['s2'][1] += 1
            elif i[2] == 's3':
                sdmg_sum['s3'][1] += 1
        elif i[1] == 'x' :
            dmg_sum['x'][1] += 1
            xdmg_sum[i[2]] += 1

    total = dmg_sum['x'][0] + dmg_sum['s']
    dmg_sum['total'] = total
    xdmg_sum['x1'] -= xdmg_sum['x5']
    xdmg_sum['x2'] -= xdmg_sum['x5']
    xdmg_sum['x3'] -= xdmg_sum['x5']
    xdmg_sum['x4'] -= xdmg_sum['x5']

    xdmg_sum['x1'] -= xdmg_sum['x4']
    xdmg_sum['x2'] -= xdmg_sum['x4']
    xdmg_sum['x3'] -= xdmg_sum['x4']

    xdmg_sum['x1'] -= xdmg_sum['x3']
    xdmg_sum['x2'] -= xdmg_sum['x3']

    xdmg_sum['x1'] -= xdmg_sum['x2']
    tmp = xdmg_sum
    xdmg_sum = {}
    for i in tmp:
        if tmp[i] != 0:
            xdmg_sum[i] = tmp[i]



    print '-----------------------'
    print "dmgsum     |", dmg_sum
    print "skill_stat |", sdmg_sum
    print "x_stat     |",xdmg_sum