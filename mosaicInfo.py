# -*- coding: utf-8 -*
import Image

img = Image.open('oxygen.png')
data = [chr(img.getpixel((i,43))[0]) for i in xrange(0,609,7)]
print ''.join(data)
nextLevel = [105,110,116,101,103,114,105,116,121]
data = [chr(i) for i in nextLevel]
print ''.join(data)