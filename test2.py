#import pandas as pd
#import json
#with open("last_active.json") as feedsjson: 
#    data = json.load(feedsjson)

#print(data)
#data2 = {}
#for key in data:
#    if data[key]>0:
#        data2[key] = data[key]-1
#    else: 
#        data2[key] = data[key]
#print(data2)

#with open("last_active.json", mode='w') as f:
#    f.write(json.dumps(data2, indent=2)) 