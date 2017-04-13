#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import os,time,threading

def home_event(driver, udid, bundleId):
    print '[ RUN ] sending HOMEKEY Event.'
    driver.send_keys('\uE105')
    def Tread():
        try:
            time.sleep(2)
            os.system('pkill -9 idevicedebug')
            print '[ RUN ] idevicedebut stop'
        except Exception ,e:
            print '\n[ ERROR ] ' + str(e) + '\n'
    threading.Thread(target=Tread).start()

    print '[ RUN ] launch App : ' + bundleId
    try:
        os.system('idevicedebug -u %s run %s)' %(udid, bundleId))
        time.sleep(3)
        return True
    except Exception ,e:
        print '\n[ ERROR ] ' + str(e) + '\n'
