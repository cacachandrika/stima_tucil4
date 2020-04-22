import re
import datetime
from datetime import date
galat = 5000

#getDate("saya anak gembala tahun 3/4/2020",5)
def getDate(text,pos):
    regexes = ['\d{1,2}-\d{1,2}-\d{4}','\d{1,2}/\d{1,2}/\d{4}',
    '\d{1,2}\s(jan|feb|mar|apr|mei|juni|juli|agt|sept|okt|nov|des)\s\d{4}',
    '\d{1,2}\s(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)\s\d{4}']
    jarak = galat if len(text)>galat else len(text)
    ans = "none"
    for j in range(len(regexes)):
        p = re.compile(regexes[j])
        for m in p.finditer(text):
            # print(m.start(), m.group())
            middle = (m.start()+m.end())/2
            if(abs(middle-pos)<jarak):
                ans = m.group()
                jarak = abs(middle-pos)
    return ans

def getTime(text,pos):
    jarak = galat if len(text)>galat else len(text)
    ans = "none"
    p = re.compile('\d{1,2}:\d{2}')
    for m in p.finditer(text):
        # print(m.start(), m.group())
        middle = (m.start()+m.end())/2
        if(abs(middle-pos)<jarak):
            ans = m.group()
            jarak = abs(middle-pos)
    return ans

def getAngka(text, pos):
    # ans = []
    # (^|\s|\()[\d\.%]+(?=\s|\))
    # match5 = re.findall(r'(?:(?<=^)|(?<=\s)|(?<=\())[\d.%]+(?=\s|\))', text)
    # match6 = re.findall(r'\d+,\d+',text)
    # match4 = re.findall(r'\d+[^/%]', text)
    # print(match5.group())
    # if(match5):
    #     # [(m.start(0), m.end(0)) for m in re.finditer(pattern, string)]
    #     ans += match5
    # return ans
    p = re.compile("(?:^|\s|\()[\d.%]+(?=\s|\))")
    jarak = galat if len(text)>galat else len(text)
    ans = "none"
    for m in p.finditer(text):
        # print(m.start(), m.group())
        middle = (m.start()+m.end())/2
        if(abs(middle-pos)<jarak):
            ans = m.group()
            jarak = abs(middle-pos)
    return ans[1:]

def Regex(text,pattern):
    match = re.search(pattern,text)
    if(match):
        return True
    else:
        return False

def getPos(text,pattern):
    ans = re.search(pattern,text)
    if(ans):
        return((ans.start()+ans.end())/2)
    return 0

# text = "8888 perilaku mudik terhadap 211.437 responden di 34 provinsi tanggal 27 jan 2020 jam 13:45 menunjukkan mayoritas responden (63%) tidak akan mudik pada perayaan Idul Fitri tahun ini. Namun, ada 12% yang menyatakan ingin mudik, 21% belum mengambil keputusan jam 8:00 dan 4% lainnya lebih dahulu pulang kampung."
# res = text.split(". ")
# # print(res)
# # # print(len(res))
# for i in range (len(res)):
# #     print(i+1)
#     date = getDate(res[i],100)
#     time = getTime(res[i],100)
#     angka = getAngka(res[i],100)
# #     tesaja(res[i])
# #     print("date")
#     print(date,time,angka)
# #     print("time")
# #     print(time)
# #     print("angka")
# #     print(angka)