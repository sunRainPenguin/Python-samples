import urllib2
import re

def getHtmlPage(url):
    return urllib2.urlopen(urllib2.Request(url)).read()

def getSmallLetters(src):
    matchList = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',src)
    return ''.join(matchList)
	
url = "http://www.pythonchallenge.com/pc/def/equality.html"
page = getHtmlPage(url)
rstList = re.findall('<!--\s+(.*)\s+-->',page,re.S)
ss = rstList[0]
result = getSmallLetters(ss)
print result