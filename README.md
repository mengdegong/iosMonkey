**1,功能**
1.可以模拟android monkey执行的方式，在IOS APP页面点击 滑动操等作,支持 ios 9和ios10
2,支持一台ios执行
下载地址:http://git.oschina.net/lvduoqiang/Blued-tools

**2,准备macaca环境**
安装usbmuxd
```
$ brew install usbmuxd
```
安装iso-webkit-debug-proxy
```
$ brew install iso-webkit-debug-proxy
```
安装iso-deploy
```
$ npm i ios-deploy -g
```
安装macacajs包括，macaca-cli macaca-ios
```
npm install macaca-cli -g
EVELOPMENT_TEAM_ID=需要填写TeamID npm install macaca-ios -g
```
检测macaca环境，无报错
```
$ macaca doctor
```

**3,WebDriverAgent项目重签名**
安装app-inspector
```
EVELOPMENT_TEAM_ID=需要填写TeamID npm install app-inspector -g
```
重签名参考帖子
[app-inspector查看器](https://testerhome.com/topics/7202)

**4,操作指南**
1,在iosMonkey/parameters/configure.py文件中设置udid/bundleId/port/proxy,port/proxy可以默认
```
bundleId = 'com.bluecity.blued.qy'
port = 3456
proxy = 8900
udid = 'bad980986e328c37e478edcc81c552d291ce4024'
version = '10.2.1'
```

2,文件中可以修改事件的概率,概率相加应是100%
```
TAP = 0.40
SWIPE = 0.30
BACK = 0.10
SUBMIT = 0.05
CONTENT = 0.05
POINT = 0.05
SHARE = 0.05
```

3,终端启动macaca服务
```
$ macaca server --verbose
```

4,运行iosMonkey/run.py,开启无限事件测试之旅
```
           #######################################
           #                                     #
           #    欢迎使用 Blued iosMonkey测试       #
           #                                     #
           #######################################

[INFO]---------------------------------------------------
[INFO]测试设备: bad980986e328c37e478edcc81c552d291ce4024 
[INFO]测试App : com.bluecity.blued.qy
[INFO]---------------------------------------------------

[ RUN ] sending Event : Content->( 201 , 391 )
[ RUN ] Event number:  1 
[ RUN ] sending Swipe Event : Swipe-> [start(302.0 , 653.0 ), end( 302.0 , 74.0)]
[ RUN ] Event number:  2 
[ RUN ] sending Event : Submit->( 177 , 596 )
[ RUN ] Event number:  3 
[ RUN ] sending Tap Event : Tap->( 303.0 , 376.0 )
```