import requests
import json
url ='https://www.izyz.org/manager/statics/indexStatics?districtId=40288188119c102f01119cadc42d01d0'
r = requests.get(url)
print(r)
dic={"name":"mcw","age":114514}
xu=json.dumps(dic)
print(xu,type(xu),type(dic))

print('------------1---------------')
