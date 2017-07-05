#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import os,time,threading

def home_event(driver, udid, bundleId):
    print '[ RUN ] sending HOMEKEY Event.'
    time.sleep(3)
    def Tread():
        driver.keys(u'\uE105')
        try:
            os.popen('pkill -9 idevicedebug')
            print '[ RUN ] idevicedebut stop'
        except Exception ,e:
            print '\n[ ERROR ] ' + str(e) + '\n'

        print '[ RUN ] launch App : ' + bundleId
        try:
            os.popen('idevicedebug -u %s run %s' %(udid, bundleId))
            time.sleep(3)
            return True
        except Exception ,e:
            print '\n[ ERROR ] ' + str(e) + '\n'
    t = threading.Thread(target=Tread)
    t.start()
    t.stop()
