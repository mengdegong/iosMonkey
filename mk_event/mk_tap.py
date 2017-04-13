#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import math,random

def tap_event(driver, width, height):
    json = {}
    x = math.ceil(random.random() * (width - 1))
    y = math.ceil(random.random() * (height - 1))
    print '[ RUN ] sending Tap Event : Tap->( %s , %s )' %(x,y)
    json['x'] = x
    json['y'] = y
    driver.touch('tap',json)
    return True
