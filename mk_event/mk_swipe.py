#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import math,random

def swipe_event(driver, width, height):
    json = {}
    startX = math.ceil(random.random() * (width - 1))
    startY = math.ceil(random.random() * (height - 1))
    entY = math.ceil(random.random() * (height - 1))
    print '[ RUN ] sending Swipe Event : Swipe-> [start(%s , %s ), end( %s , %s)]' %(startX, startY, startX, entY)
    json['fromX'] = startX
    json['fromY'] = startY
    json['toX'] = startX
    json['toY'] = entY
    json['duration'] = 1
    driver.touch('drag', json)
    return True

