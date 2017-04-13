#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random

def bake_event(driver,backX,backY):
    json = {}
    print '[ RUN ] sending Event : Back->( %s , %s )' %(backX,backY)
    json['x'] = backX
    json['y'] = backY
    driver.touch('tap',json)
    return True

