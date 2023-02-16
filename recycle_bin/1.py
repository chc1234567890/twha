import json
import copy

f=open("provinces_old.js","r")
a=json.loads(f.read())
f.close()
f=open("positions.txt","r")
while True:
    s=f.readline()
    if not s:
        break
    s=s.split(' ')
    for i in range(len(a)):
        if(a[i]['x']==int(s[3]) and a[i]['y']==int(s[4])):
            a[i]['id']=int(s[0])
f.close()
d=dict()
for i in a:
    id=i['id']
    tmp=copy.copy(i)
    del tmp['id']
    d[id]=tmp
f=open("provinces.txt","r",encoding="utf-8")
while True:
    s=f.readline()
    if not s:
        break
    v=s.split('\t')
    id=int(v[0])
    # print(id)
    try:
        d[id]['zhname']=v[2]
        d[id]['file']=v[4]
        if(v[7]=="水域"):
            d[id]['region']="SEA"
        else:
            d[id]['region']=v[8].split(',')[0]
    except KeyError:
        pass
        # print('Error %d' % id)
print(str(d).replace(', ',',').replace(': ',':'))