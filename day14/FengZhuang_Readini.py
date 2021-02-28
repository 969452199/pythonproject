import configparser
import os

class ReadConf():
    def __init__(self):
        curpath = os.path.dirname(os.path.relpath(__file__))
        #获取配置文件路径
        cfgpath = os.path.join(curpath, "config.ini")

        # 创建管理对象
        self.conf = configparser.ConfigParser()
        # 读ini文件
        self.conf.read(cfgpath, encoding="utf-8")

    def readConf(self,param):
        #获取所有的section
        # sections = self.conf.sections()
        # print(sections)
        #获取某个sections中的所有值,将其转化为字典
        items = dict(self.conf.items(param))
        return items

if __name__ == '__main__':
    test = ReadConf()
    t = test.readConf("login")   #传入sections的值
    print('我取某个sections下所有值 ',t)
    print(t['username'])