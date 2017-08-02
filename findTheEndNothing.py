import urllib2
import re

def getHtmlPage(url):
    return urllib2.urlopen(urllib2.Request(url)).read()
	
urlHead = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
urlTail = "8022";
page = getHtmlPage(urlHead+urlTail)
listPage = page.split()
print page
while str(listPage[len(listPage)-1]).isdigit():
    newUrl = urlHead + str(listPage[len(listPage)-1])
    page = getHtmlPage(newUrl)
    print page
    listPage = page.split()
	
