import requests
import json
import sys
import time
code = ""

print("using sheetid: " + code)

def get_name(size):
        ret = []
        try:
                data = json.loads(requests.get("https://uinames.com/api/?ext&amount={}&region=united+states&gender=random&source=uinames.com".format(size)).text)
        except:
                print("wait!")
                time.sleep(70)
                return []
        for x in data:
                ret.append(x["name"] + " " + x["surname"])
        return ret

def login(name):
        return requests.post("http://signinnow.jimmyli.us/api/signin", json={"name": name, "sheetid": code}).text
while True:
        for x in get_name(500):
                print(login(x))
