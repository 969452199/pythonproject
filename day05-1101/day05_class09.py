import json
class data:

    def __init__(self,file_path = None):
        if file_path == None:
            self.file_path = "G:\\pythonproject\\info.json"
        else:
            self.file_path = file_path
        self.dat = self.read_json()
    def read_json(self):
        with open(self.file_path) as fp:
            dat = json.load(fp)
            return dat


    def get_json(self,id):
        return self.dat[id]

    def write_json(self,dat):
        with open("G:\\pythonproject\\afternoom.json") as fp:
            fp.writelines(json.dumps(dat))
if __name__=='__main__':
    # opecjson = data()
    # print(opecjson.get_json('sed'))
    # print(opecjson.get_json('age'))
    # print(opecjson.get_json('class'))
    op = data(file_path='G:\\pythonproject\\afternoom.json')
    print(op.get_json('foot'))
    # opecjson.write_json({"qw":1})



