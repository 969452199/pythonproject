import  xml.dom.minidom


class xml1():
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'G:\\pythonproject\\day06-11-15\\abc.xml'
        else:
            self.file_path = file_path
        self.dom = xml.dom.minidom.parse('abc.xml')

    def get_word(self,weord):
        try:
            root = self.dom.documentElement
            bb = root.getElementsByTagName(weord)
            for i in range (len(bb)):
                b = bb[i]
#            b = bb[0]
            return b.nodeName
        except BaseException as e1:
            return e1


    def biaoqian(self,biaoqianming,word2):
        try:
            root = self.dom.documentElement
            itemlist = root.getElementsByTagName(biaoqianming)
            item = itemlist[0]
            un = item.getAttribute(word2)
            return un
        except BaseException as e2:
            return e2

    def qitaword(self,word3):
        try:
            root = self.dom.documentElement
            cc = self.dom.getElementsByTagName(word3)
            cv = []
            for t in range(0, len(cc)):
                ce = cc[t]
                ct = ce.firstChild.data
                cv.append(ct)
            return cv
        except BaseException as e3:
            return e3
p = xml1('abc.xml')
u = p.get_word('maxid')
print(u)
u1 = p.biaoqian('login','username')
print(u1)
u2 = p.qitaword('caption')
print(u2)
