import time
print(time.time())   #1605430837.309023
print(time.localtime())
print(time.mktime(time.localtime()))    #1605430837.0
print(time.gmtime(time.time()))
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
print(time.strftime("%Y-%m-%d %X",time.localtime()))   #2020-11-15 17:03:12
time.asctime(time.localtime())
print(time.ctime(time.time()))   #Sun Nov 15 17:04:04 2020



from datetime import  *
dt = datetime.now()
d1 = dt + timedelta(days=-1)  #昨天
print(d1)
d2 = dt - timedelta(days=1)   #昨天
print(d2)
d3 = dt + timedelta(days=1)   #明天
print(d3)
d4 = d3-dt
print(type(d4),d4)
print(d4.days,d4.total_seconds())