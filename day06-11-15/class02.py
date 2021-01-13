import yaml
import os

curpath = os.path.dirname(os.path.realpath(__file__))
#yamlpath = os.path.join(curpath,"yamltext.yaml")

class yamltext():
    def __init__(self,feilpath=None):
        if feilpath = None:
            feilpath = os.path.join(curpath,"yamltext.yaml")
        else:
            feilpath = feilpath
        self.file1 = open(feilpath,'r',encoding='utf-8')

    def file(self):
        try:
            sfg = self.file1.read()
            sf = yaml.load(sfg)
            return sf
        except BaseException as e1:
            return e1

    def write(self):
        try:
            self.file2 = open(feilpath,'a',encoding='utf-8')
            data = {"NIULIU": {'age': 18, 'gread': 3, 'class': 6}}
            yaml.dump(data, fw)
            dc = self.file1.read()
            dc1 = yaml.load(dc)
            return dc1
        except BaseException as e2
            return e2

if __name__ == "__main__":
    e = yamltext()


