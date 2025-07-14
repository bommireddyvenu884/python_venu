#pip3 install faker

from faker import Faker
data = Faker()
data.emial()
data.country()
data.random_int()
data.profile()


#json module helps to convert dict to json  and vice.
#json.dumps ==> take data and converts to json 
#json.dump ==> take json file write into dictpip 
#json.loads ==>take json string and comvertinto dict
#json.load ==> take json file and convert to dict

import json
dir(json)

#converting dict into json.
 x = data.profile()
 print(x)
 print(json.dumps(x,default=str))
 print(json.dumps(x,default=str,indent=2))


 #json.loads ==>take json string and comvertinto dict
 json.loads(jsondata)