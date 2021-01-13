'''字典,{'key1':'value1','key2':'value2'}'''

d = {'shanghai':'021','nanchang':'0791','hangzhou':'0571'}
print(type(d))
a = {1:'a',2:['a','b'],(2,):['a','b'],"hello":{1:'a'},1:'python'}#键出现重复时，后面的会覆盖前面的
print(a)

#b = {[1,2]:'hello'},列表可以修改，不能作为key，元组不可修改，可以
#print(b)
e = {(1,2):'hello'}
print(e)

b = dict(a=1,b=2,c=3)
print(b)

print(d)
print(d['shanghai'])
d['shanghai'] = '123'#修改键值对的值
print(d)
d['beijing'] = '010'#在字典内添加键值对，方法为【’key‘】=’value‘
print(d)



#通过key获取value
print(d.get('shanghai'))
print(d.setdefault('shanghai'))

d1 = dict(a=1,b=2)
d1.update(d)#增加键值对（拼接2个键值对）
print(d1)
d1.pop('a')#删除指定键值对
print(d1)
d1.popitem()#从后往前删
print(d1)



q = dict(a=2,b=3,c=4,d=5)
print(q)
print(q.get('c'))
print(q.setdefault('c','d'))
w = dict(q=4,w=5,e=5)
w.update(q)
print(w)
e = dict(r=1,t=3)
q.update(e)
print(q)

q.pop('r')
print(q)
q.popitem()
print(q)
q.clear()
print(q)


