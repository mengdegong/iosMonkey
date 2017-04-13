#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random

def share_event(driver, width):
    json = {}
    x = width / 10
    y = 25
    print '[ RUN ] sending Event : Share->( %s , %s )' %(x, y)
    json['x'] = x
    json['y'] = y
    driver.touch('tap',json)
    return True