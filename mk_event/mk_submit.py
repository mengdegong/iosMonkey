#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random

#目测和mk_content一致

def submit_event(driver, submitX_max, submitX_mim, submitY_max, submitY_mim):
    json = {}
    x = random.randint(0,submitX_max) % (submitX_max - submitX_mim + 1) + submitX_mim
    y = random.randint(0,submitY_max) % (submitY_max - submitY_mim + 1) + submitY_mim
    print '[ RUN ] sending Event : Submit->( %s , %s )' %(x, y)
    json['x'] = x
    json['y'] = y
    driver.touch('tap',json)
    return True

