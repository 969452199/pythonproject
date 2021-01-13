import yaml
import os

#获取当前脚本所在文件路径
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
yamlpath = os.path.join(curpath,"yamltext.yaml")


f = open(yamlpath,'r',encoding='utf-8')
cfg = f.read()
print(type(cfg)) #读出来是字符串
print(cfg)
print(yaml.load(cfg,Loader=yaml.FullLoader))
