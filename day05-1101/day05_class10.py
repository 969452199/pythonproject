import configparser

config = configparser.ConfigParser()#实例化格式
path = 'G:\\pythonproject\\config.ini'
config.read(path)

class sec:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "G:\\pythonproject\\config.ini"
        else:
            self.file_path = file_path
        self.data = self.read.ini()
    def read_ini(self):
        config.read(path)
        value = config[section][key]
        return value
f = sec.read_ini(['login']['username'])
print(f)