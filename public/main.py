from kmp import *
from bm import *
from regex import * 
import sys
import redis
import json

class Result:
    def __init__(self, date, time, angka, kalimat, namafile):
        self.date = date
        self.time = time
        self.angka = angka
        self.kalimat = kalimat
        self.namafile = namafile

    def getJson(self):
        return {
            "date": self.date, 
            "time": self.time, 
            "jumlah": self.angka, 
            "kalimat": self.kalimat, 
            "filename": self.namafile
        }

jobid = sys.argv[1]
r = redis.Redis(
    host='127.0.0.1',
    port=6379, 
    password='')
value = r.get(jobid)
y = json.loads(value)
pattern = y["keyword"]
for i in range(len(y["filenames"])):
    f = open(y["filenames"][i], "r")
    teks = f.read()
    teks.rstrip()
    kalimat = teks.split(". ")
    #print("panjang array kalimat")
    #print(len(kalimat))
    for j in range (len(kalimat)):
        #print("value of j:",j)
        found = False
        date = getDate(teks,getPos(teks,pattern))
        time = getTime(teks,getPos(teks,pattern))
        angka = getAngka(teks,getPos(teks,pattern))
        sentences = kalimat[j].strip("\n").strip()
        if(y["algo"]=="Regex"):
            found = Regex(sentences,pattern)
        elif(y["algo"]=="KMP"):
            found = KMP(sentences,pattern)
        elif(y["algo"]=="Boyer-Moore"):
            found = boyer(sentences,pattern)
        #print(boyer(sentences,pattern))
        print(found)
        if(found):
            # yg disimpen date, time, angka, kalimat[j], y[filename][i]
            res = Result(date,time,angka,kalimat[j],y["filenames"][i])
            y["result"].append(res.getJson())
            # print(y)
r.set(jobid, json.dumps(y))