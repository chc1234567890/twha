import json
import copy

f=open("path_old.js","r")
a=json.loads(f.read())
d=dict()
f.close()
for i in range(len(a)):
    d[i+1]=a[i]
print(str(d).replace(', ',',').replace(': ',':'))
print(len(str(d).replace(', ',',').replace(': ',':')))
print(len(d))