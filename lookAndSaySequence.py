# -*- coding: utf-8 -*

def getNext(prv):
    temp = prv[0]
    num = 0
    result = ''
    for ch in prv:
        if(ch==temp):
            num = num+1
        else:
            result = result+str(num)+temp
            temp = ch
            num = 1
    result = result + str(num) + temp
    return result
	
input = '1'
for index in range(30):
    input = getNext(input)

print len(input)
