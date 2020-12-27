import json
'''with open('G:\\pythonproject\\info.json','r',encoding='utf-8') as fp:
    json_data = json.load(fp)
    print('文件数据是：',json_data)
    print('数据类型：',type(json_data))
#写入
dict = {'name':'ming','age':17,'class':4}
with open('G:\\pythonproject\\info.json','w',encoding='utf-8') as fp:
    json.dump(dict,fp,ensure_ascii=False)
with open('G:\\pythonproject\\info.json','r',encoding='utf-8') as fp:
    json_data = json.load(fp)
    print('文件数据是：',json_data)
    print('数据类型：',type(json_data))'''

#转换，字符串转换成字典
str1 = '{"name":"yu","age":20,"class":5}'
print('字符串转换成字典后的数据：',json.loads(str1))
print(type(json.loads(str1)))
#转换，字典转换成字符串(json)
dict1 = {"name":"wang","age":19,"class":4}
print('字典转换成json后数据：',json.dumps(dict1,ensure_ascii=False))
print(type(json.dumps(dict1)))
