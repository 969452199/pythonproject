import yaml
import os

#获取当前脚本所在文件路径
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)

#获取yaml文件路径
yamlpath = os.path.join(curpath,"yamltext.yaml")

#open方法打开直接读出来
f = open(yamlpath,'r',encoding='utf-8')
cfg = f.read()
print(type(cfg)) #读出来是字符串
print(cfg)

#读出来是字符串形式，不是字典，要转换成字典可以用load
d = yaml.load(cfg)
print(d)
print(type(d))
#写入yaml文件
#a是追加写入，w 覆盖写入
fw = open(yamlpath,'a',encoding='utf-8')
#构建数据
data = {"WANGWU":{'age':18,'gread':3,'class':6}}
#装载数据
yaml.dump(data,fw)
#读取数据，获取文件
f = open(yamlpath,'r',encoding='utf-8')
#读取文件
cong = yaml.load(f.read())
print(cong,Loader=yaml.FullLoader)
