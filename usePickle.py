# -*- coding: utf-8 -*
import urllib2
import re
import pickle

def getHtmlPage(url):
    return urllib2.urlopen(urllib2.request(url)).read()
	
url = "http://www.pythonchallenge.com/pc/def/banner.p"
page = urllib2.urlopen(url).read()
plist = pickle.loads(page)
for item in plist:
    print ''.join(i[0]*i[1] for i in item)    # 这里每个list的item都是一行的内容
	
