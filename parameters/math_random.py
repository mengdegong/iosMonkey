#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random
from configure import *

class random_math():
    def __init__(self):
        self.EVENT_TYPE_TAP = TAP
        self.EVENT_TYPE_SWIPE = SWIPE
        self.EVENT_TYPE_BACK = BACK
        self.EVENT_TYPE_SUBMIT = SUBMIT
        self.EVENT_TYPE_CONTENT = CONTENT
        self.EVENT_TYPE_SPECIAL_POINT = POINT
        self.EVENT_TYPE_SHARE = SHARE
        self.EVENT_TYPE_HOME = HOME

    def percentage_random(self):
        random_number = random.random()
        if random_number >= 0 and random_number <= self.EVENT_TYPE_TAP:
            return 0
        elif random_number >= self.EVENT_TYPE_TAP and random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE:
            return 1
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK:
            return 2
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT:
            return 3
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT \
                + self.EVENT_TYPE_CONTENT:
            return 4
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT + self.EVENT_TYPE_CONTENT <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT \
                + self.EVENT_TYPE_CONTENT + self.EVENT_TYPE_SPECIAL_POINT:
            return 5
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT + self.EVENT_TYPE_CONTENT \
                + self.EVENT_TYPE_SPECIAL_POINT <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT \
                        + self.EVENT_TYPE_CONTENT + self.EVENT_TYPE_SPECIAL_POINT + self.EVENT_TYPE_SHARE:
            return 6
        elif self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT + self.EVENT_TYPE_CONTENT \
                + self.EVENT_TYPE_SPECIAL_POINT + self.EVENT_TYPE_SHARE <= random_number <= self.EVENT_TYPE_TAP + self.EVENT_TYPE_SWIPE + self.EVENT_TYPE_BACK + self.EVENT_TYPE_SUBMIT \
                        + self.EVENT_TYPE_CONTENT + self.EVENT_TYPE_SPECIAL_POINT + self.EVENT_TYPE_SHARE + self.EVENT_TYPE_HOME:
            return 7
        return -1
