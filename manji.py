# coding=utf-8
from selenium import webdriver
import time
import requests
from lxml import etree
from urllib import request

USERNAME = ''
PASSWORD = ''
#class_name_list=[]
class FILE:
    def __init__(self):
        self.f = open("满绩经.txt", "w+")
        self.driver = webdriver.Chrome()
        self.driver.get("http://jwbinfosys.zju.edu.cn/")
    
    def login(self):
        time.sleep(11)
        self.driver.find_element_by_xpath('//*[@id="Form1"]/div[2]/div[2]/h5/div/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(USERNAME)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
        self.driver.find_element_by_xpath('//*[@id="dl"]').click()
        time.sleep(11)
        self.driver.find_element_by_xpath('//*[@id="Button1"]').click()
        self.driver.find_element_by_xpath('//*[@id="xsmain_wsxk.htm"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="list_byjy"]/li[1]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('//*[@id="navbar-nav"]/li[2]/a').click()
        time.sleep(3)

    def get_class_list(self):
        element=self.driver.find_element_by_xpath('//*[@id="contentBox"]') # 收起第一个
        n=5
        while(n>0):
            try:
                self.driver.find_element_by_xpath('//*[@id="nextPage"]').click()
            except:
                pass
            n=n-1
        self.driver.find_element_by_xpath('//*[@id="contentBox"]/div/div[1]/div[1]').click()
        time.sleep(5)
        class_list=element.find_elements_by_tag_name('a')
        for oneclass in class_list:
            if oneclass.text not in  ["展开关闭",""]:
            #   class_name_list.append(oneclass.text)
                self.f.write(oneclass.text+'满绩,')

    def get_tongshi(self):
        self.f.write('通识满绩\n')
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[4]/ul/li[1]/a').click()
        self.get_class_list()

    def get_xintongshi(self):
        self.f.write('\n新通识满绩\n')
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[5]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[5]/ul/li[1]/a').click()
        self.get_class_list()
    
    def get_tiyu(self):
        self.f.write('\n体育满绩\n')
        self.driver.find_element_by_xpath('//*[@id="tykTool"]').click()
        self.get_class_list()
    
    def get_zhuanyejichu(self):
        self.f.write('\n专业基础课程满绩\n')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[8]/a').click()
        self.get_class_list()
    
    def get_dalei(self):
        self.f.write('\n大类课程满绩\n')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[9]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[9]/ul/li[1]/a').click()
        self.get_class_list()
    
    def get_zhuanye(self):
        self.f.write('\n专业课程满绩\n')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[10]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[10]/ul/li[2]/a').click()
        self.get_class_list()

    def get_zhuyuan(self):
        self.f.write('\n竺院课程满绩')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[11]/a').click()
        self.get_class_list()

    def get_rongyu(self):
        self.f.write('\n荣誉课程满绩\n')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[12]/a').click()
        self.get_class_list()

    def get_teshu(self):
        self.f.write('\n特殊课程满绩\n')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[19]/a').click()
        self.driver.find_element_by_xpath('//*[@id="nav_tab"]/li[13]/a').click()
        self.get_class_list()

if __name__=='__main__':
    t=FILE()
    t.login()
    t.get_tongshi()
    t.get_xintongshi()
    t.get_tiyu()
    t.get_zhuanyejichu()
    t.get_dalei()
    t.get_zhuanye()
    t.get_zhuyuan()
    t.get_rongyu()
    t.get_teshu()










 