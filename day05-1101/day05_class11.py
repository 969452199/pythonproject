#读取ini文件
import configparser

config = configparser.ConfigParser()#实例化格式
path = 'G:\\pythonproject\\config.ini'
config.read(path)
value = config['login']['username']
print(value)

value = config.get('test','a')
print(value)

value = config.items('test')
print(value)


value = config.sections()
print(value)
for i in value:
    print(config.items(i))

config.set('login','username','admin1')
# config.add_section('sale')
# config.set('sale','shupain','5')
# config.set('sale','huotui','2')
# config.write(open(path,'w'))

