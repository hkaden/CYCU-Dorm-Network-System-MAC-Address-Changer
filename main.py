# -*- coding: utf-8 -*-
import urllib,urllib2,cookielib

def loginWeb(site):
    LoginValue={
                'action':'register',
                'mpwd':'Zxcv19710412563',
                'student_id':'10427271',
                'zh_tw':'0'
               }

    #使用cookielib自動管理cookie
    cj=cookielib.CookieJar()
    opender=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #偽裝成mac osx
    opender.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')]
    #把結果綁到變量
    re=opender.open(site,urllib.urlencode(LoginValue))
    print cj

    """
    #登陆成功之后的带着cookie的页面访问
    pc='https://console.oray.com'#比如个人中心页面
    pcre=opender.open(pc)
    print pcre.getcode()
    print pcre.read()
    """


if __name__ == '__main__':

    site='http://ccdna.cycu.edu.tw/register_dorm/activate.php'
    #user='uname'
    #password='upwd'
    loginWeb(site)
