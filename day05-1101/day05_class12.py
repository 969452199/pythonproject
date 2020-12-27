import  configparser

def read_ini(sections1,key,value=None):#当value有时要输入有时不输入时，可以用默认参数
    config = configparser.ConfigParser()
    config.read('G:\\pythonproject\\config.ini')
    if sections1 in config.sections():
        value = config[sections1][key]
        #print(value)
        return value
    else:
        config.add_section(sections1)
        config.set(sections1,key,value)
        config.write(open('G:\\pythonproject\\config.ini', 'w'))
a = read_ini('ss','er','23')
print(a)
