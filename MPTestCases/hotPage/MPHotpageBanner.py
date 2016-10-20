#coding:utf-8
'''
Created on 2016年10月12日

@author: wenjing
'''

import sys
curDir = sys.path[0]
print curDir
sys.path.append(curDir + '\\MPTestCases\\common')

import unittest
from appium import webdriver
from time import sleep
import Initialize

class MPHotpageBanner(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)
        print "************************** MPBanner_test test **************************"

    def setUp(self):
        desired_caps={}
        desired_caps['device']='android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='69T7N15B26001273'
        #desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
        #被测试的App在电脑上的位置
        desired_caps['appPackage']='com.yixia.videoeditor'
        desired_caps['appActivity']='.ui.login.SplashActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit();
        print 'end ... '

    def test_banner(self):
		try:
			print 'start test_banner test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在
			sleep(7)
			#查找banner翻页元素获取banner总页数
			eles=self.driver.find_elements_by_xpath('//android.widget.LinearLayout[contains(@id,com.yixia.videoeditor:id/banner_dots_layout)]/android.widget.ImageView')
			l=len(eles)*2
			print l
			#获取banner元素
			banner=self.driver.find_element_by_id('com.yixia.videoeditor:id/banner_img')
			#向左滑动banner总数*2次
			width=self.driver.get_window_size().get('width')
			height=self.driver.get_window_size().get('height')
			#print width
			#print height
			x_start=540*width/720
			x_end=160*width/720
			y=450*height/1280
			for i in range(0,l):
				self.driver.swipe(x_start, y, x_end, y)
				sleep(2)
			#向左滑动banner总数*2次
			for i in range(0,l):
				self.driver.swipe(160, 450,546, 409)
				sleep(2)
			sleep(5)
			#点击任一banner
			banner.click()
			self.driver.keyevent('4')
			sleep(5)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

def suite(self):
     suite = unittest.TestSuite()  
     suite.addTest(MPHotpageBanner('test_banner'))
     runner = unittest.TextTestRunner()  
     runner.run(suite)       
        