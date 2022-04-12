import requests
import json

def getHashes(uuid):
        response = requests.get(f"https://urlscan.io/api/v1/result/{uuid}/")._content
        data = json.loads(response)
        s = json.dumps(data)
        f = open(f"{uuid}.json","a")
        f.write(s)
        f.close()
        f = open(f"{uuid}.json","r")
        ff = json.load(f)
        for x in ff["lists"]["hashes"]:
            occurency(x)
     

def fecthData(domainAddress):
    response = requests.get(f"https://urlscan.io/api/v1/search/?q=domain:{domainAddress}")._content
    data = json.loads(response)
    s = json.dumps(data)
    f = open(f"{domainAddress}.json","a")
    f.write(s)
    f.close()
    f = open(f"{domainAddress}.json","r")
    ff = json.load(f)
    for x in ff["results"]:
        try:
            getHashes(x["task"]["uuid"])
        except:
            pass

occDict = {}

def occurency(hash):
    if hash in occDict.keys():
        occDict[hash] += 1
    else:
        occDict[hash] = 1

fileName = input("file that contains domain addresses : ")
file = open(f"{fileName}","r")
for x in file:
    fecthData(x.split("\n")[0].strip())

print(occDict)