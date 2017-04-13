#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random

def content_event(driver, contentX_max, contentX_min, contentY_max, contentY_mim):
    json = {}
    x = random.randint(0,contentX_max) % (contentX_max - contentX_min + 1) + contentX_min
    y = random.randint(0,contentY_max) % (contentY_max - contentY_mim + 1) + contentY_mim
    print '[ RUN ] sending Event : Content->( %s , %s )' %(x, y)
    json['x'] = x
    json['y'] = y
    driver.touch('tap',json)
    return True
