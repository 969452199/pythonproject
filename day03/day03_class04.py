song = "when I am down and oh my soul so weary When troubles come and my heart burdened be Then I am still and  wait here in the silence Until you come and sit awhile with me You raise me up so I can stand on mountains YOu raise me up to walk on stormy  sears I am strong when I am on your shoulders You raise me up to more  than I can be You raise me up so I can stand on mountains Your raise me  up to walk on stormy seas I am strong when I am on your shoulders You  raise me up to more than I can be You raise me up so I can stand on  mountains"
song1 = song.lower()
print(song1)
a = song1.split()
print(a)
d = { }
for word in a:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)







