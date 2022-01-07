import json
from math import radians, pi, sin, cos, sqrt, asin
from collections import defaultdict

def find_dist(latlng_1, latlng_2):
    # print(latlng_1[0],latlng_1[1])
    lat1, lon1 = radians(latlng_1[0][0]), radians(latlng_1[0][1])
    lat2, lon2 =  radians(latlng_2[0][0]), radians(latlng_2[0][1])
    d = 2*6371*asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2))
    
    return round(d,2)

file = "new1.json"
#currencies": [{"code": "LKR", "name": "Sri Lankan rupee", "symbol": "Rs"}]
#currencies": [{"code": "MGA", "name": "Malagasy ariary", "symbol": "Ar"}]
#currencies": [{"code": "INR", "name": "Indian rupee", "symbol": "\u20b9"}
limit = 277500

with open(file, 'r') as f:
    contries = json.load(f)
first_20 = {}
d2=defaultdict(lambda:0)
for contry in contries:
    d2[contry['currencies'][0]['code']]+=1
for contry in contries:
    if contry['population'] >= limit and d2[contry['currencies'][0]['code']]==1:
        first_20[contry['alpha3Code']] = []
        first_20[contry['alpha3Code']].append(contry['latlng'])
        first_20[contry['alpha3Code']].append(contry['population'])
        # first_20[contry['alpha3Code']].append(contry['currencies'][0]['code'])
        # if len(first_20)==20:
        #     break
# print(d2)
# print(len(d2))
first_20=dict(sorted(first_20.items(),key=lambda x:x[1][1])[:20])
print(first_20,len(first_20))
total_dist = 0
keys = list(first_20.keys())
# print(keys)
N=len(keys)
for i in range(N):
    for j in range(i+1,N):
        total_dist += find_dist(first_20[keys[i]], first_20[keys[j]])
total_dist = round(total_dist, 2)


print(total_dist)