# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import uuid
import urllib,urllib2,cookielib

def loginWeb(site,username,password,mac,ip):
    LoginValue={
                'action':'register',
                'mpwd': password,
                'student_id': username,
                'zh_tw':'0'
               }

    #使用cookielib自動管理cookie
    cj=cookielib.CookieJar()
    opender=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #偽裝成mac osx
    opender.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')]
    #把結果綁到變量
    re=opender.open(site,urllib.urlencode(LoginValue))
    #print re.read()
    '''
    data=BeautifulSoup(re.read())
    found = data.find('input')['value']
    print data.find(name="ipAddr")['value']
    #print cj
    '''

    ChangeMacValue={
                'ipAddr':ip,
                'status':'%A5%BF%B1%60%A8%CF%A5%CE%A4%A4',
                'macAddr':mac,
                'update_mac':'update'
               }
    #登陆成功之后的带着cookie的页面访问
    pc='http://ccdna.cycu.edu.tw/register_dorm/activate.php'#比如个人中心页面
    pcre=opender.open(pc,urllib.urlencode(ChangeMacValue))
    print pcre.getcode()
    print pcre.read()



if __name__ == '__main__':
    site='http://ccdna.cycu.edu.tw/register_dorm/activate.php'
    username=raw_input(">>> Input Username: ")
    password=raw_input(">>> Input Password: ")
    ip=raw_input(">>> Input Your IP: ")
    mac=raw_input(">>> Input Mac you want: ")
    loginWeb(site,username,password,mac,ip)
