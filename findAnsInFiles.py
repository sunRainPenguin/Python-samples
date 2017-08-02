import zipfile

f = open('channel/90052.txt','r')
str = f.read()
strList = str.split()
endingStr = strList[len(strList)-1]
print endingStr
while endingStr.isdigit():
    f = open('channel/'+endingStr+'.txt','r')
    str = f.read()
    strList = str.split()
    endingStr = strList[len(strList)-1]
    print str
	
print '*************** find the answers in zip file comments *********************'

zipObj = zipfile.ZipFile('channel.zip')
fileName = '90052.txt'
zipCmtList = []
while True:
    zipinfo = zipObj.getinfo(fileName)
    zipCmtList.append(zipinfo.comment)
    f= open('channel/' + fileName,'r')
    str = f.read()
    strList = str.split()
    if strList[-1].isdigit():
        fileName = strList[-1]+'.txt'
    else:
        break
		
print ''.join(zipCmtList)
    
	

	
