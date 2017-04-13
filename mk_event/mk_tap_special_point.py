#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

def tap_point_event(driver, special_point_x, special_point_y):
    json = {}
    print '[ RUN ] sending SpecialPoint Tap Event : Tap->( %s , %s )' %(special_point_x,special_point_y)
    json['x'] = special_point_x
    json['y'] = special_point_y
    driver.touch('tap',json)
    return True
