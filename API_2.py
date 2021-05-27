import pymongo
import requests
import json

#Database_part
# myclient = pymongo.MongoClient('10.10.153.169', 27017)
#
# mydb = myclient["sqepsng80"]
# mycol = mydb["adminsettings"]
# for x in mycol.find():
#     print(x)
#print(mycol.count())

#API_part
sess = requests.session()
url = "https://10.10.153.169/eps/login"
data = {"username":"automation@yopmail.com","password":"Quick@1234","submit":"Sign in"}
response = sess.post(url,data=data,verify=False)
#print(response.text)
# resp_json = json.loads(response.text)
# print(resp_json)

if response.status_code == 200:
    resp = sess.get('https://10.10.153.169/eps/v1/epsuser/role/count', verify=False)
    if resp.status_code == 200:
        print(resp.text)
        # data_dict = json.loads(resp.text)
        # print(data_dict)


