#coding=utf-8
import  xml.dom.minidom

dom = xml.dom.minidom.parse('abc.xml')

root = dom.documentElement
#print(root.nodeName)
bb = root.getElementsByTagName('maxid')
b = bb[0]
print(b.nodeName)

bb = root.getElementsByTagName('login')
b = bb[0]
print(b.nodeName)
ur = b.getAttribute("username")
print(ur)
pd=b.getAttribute("passwd")
print (pd)

ii = root.getElementsByTagName('item')
i1 = ii[0]
i=i1.getAttribute("id")
print (i)

i2 = ii[1]
i=i2.getAttribute("id")
print (i)


cc = dom.getElementsByTagName('caption')
c1=cc[0]
print(c1.firstChild.data)
c2=cc[1]
print(c2.firstChild.data)


