#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

from macaca import WebDriver
import configure
from math_random import *
from mk_event.mk_tap import *
from mk_event.mk_swipe import *
from mk_event.mk_submit import *
from mk_event.mk_launch import *
from mk_event.mk_home_key import *
from mk_event.mk_content import *
from mk_event.mk_bake import *
from mk_event.mk_tap_special_point import *
from mk_event.mk_share import *

class monkey():
    def __init__(self):
        self.backX = 25
        self.backY = 40

    def info(self):
        print  "\n           "+"#######################################\n"+ \
                	    "           #                                     #\n"+ \
                		"           #    欢迎使用 Blued iosMonkey测试       #\n"+ \
                		"           #                                     #\n"+ \
                		"           #######################################"

        print '\n[ INFO ]---------------------------------------------------'
        print '[ INFO ]测试设备: %s \n[ INFO ]测试App : %s' %(configure.udid,configure.bundleId)
        print '[ INFO ]---------------------------------------------------\n'
        os.system('pkill -9 proxy')
        try:
            monkey().run_event()
        except Exception ,e:
            print "\n[ ERROR ]---------------------------------------------------\n" +\
                        "[ ERROR ]"+str(e)+"\n"+\
                        "[ ERROR ]---------------------------------------------------"

    def run_event(self):
        driver = monkey().start
        eventfun = 0
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        submitX_max = width - 1
        submitX_mim = width / 10
        submitY_max = height - 1
        submitY_mim = height / 10 * 9

        contentX_max = width - width / 10
        contentX_mim = width / 10;
        contentY_max = height / 2 + height / 10
        contentY_mim = height / 2 - height / 10

        special_point_x = width / 2
        special_point_y = int(height * 0.94)

        while True:
            num = random_math().percentage_random()
            if  num ==0:
                tap_event(driver, width, height)

            elif num ==1 :
                swipe_event(driver, width, height)

            elif num ==2 :
                bake_event(driver, self.backX, self.backY)

            elif num ==3 :
                submit_event(driver, submitX_max, submitX_mim, submitY_max, submitY_mim)

            elif num ==4 :
                content_event(driver, contentX_max, contentX_mim, contentY_max, contentY_mim)

            elif num == 5 :
                tap_point_event(driver, special_point_x, special_point_y)

            elif num == 6:
                share_event(driver, width)
            elif num == 7:
                home_event(driver, udid, bundleId)

            eventfun = eventfun + 1
            print '[ RUN ] Event number:  %d ' %eventfun


    @property
    def start(self):
        porps = {}
        server = {}

        porps['platformName'] = 'iOS'
        porps['platformVersion'] = configure.version
        porps['deviceName'] = 'iPhone 6s'
        porps['autoAcceptAlerts'] = True
        porps['udid'] = configure.udid
        porps['bundleId'] = configure.bundleId
        # porps['proxyPort'] = configure.proxy

        server['hostname'] = '127.0.0.1'
        server['port'] = configure.port

        try:
            print porps
            print server
            self.driver = WebDriver(porps, server)
            self.driver.init()
            return self.driver
        except Exception ,e:
            print "\n[ ERROR ] ---------------------------------------------------" +\
                    "\n[ ERROR ] macaca server 启动失败\n"+\
                    "[ ERROR ] ---------------------------------------------------\n"

        # 守护进程
        # finally:
        #     print '8888'
        #     self.driver.init()
        #     time.sleep(5)
        #     monkey().run_event()
        #     print '[ RUN ] 守护进程启动成功'



