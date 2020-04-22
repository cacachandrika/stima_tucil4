def last(chr, hash):
    try:
        return hash[chr]
    except KeyError:
        return -1

def boyer(text, pattern):
    hash = {}
    arr = pattern
    for i in range(len(pattern)):
        hash[pattern[i]]=i
    # #print('hash',hash)
    n = len(text)
    m = len(pattern)
    i = m-1
    j = m-1
    while(i<n):
        if(pattern[j]==text[i]):
            if(j==0):
                return True
            else:
                i-=1
                j-=1
        else:
            lastt = 1+last(text[i],hash)
            i=i+m-min(j,lastt)
            j=m-1
    return False

# def find(pattern, chr):
#     m = len(pattern)
#     # #print("masu")
#     for i in range(m-2,0,-1):
#         # #print(chr,pattern[i])
#         if(chr == pattern[i]):
#             #print("yg sama", i)
#             return i
#     return -1

# txt = "Masa pandemi Covid-19 dianggap sebagai waktu yang paling tepat untuk berpesta durian, khususnya durian musang king"
# pat = "paling tepat"
# arr = txt.split(".")
# #print(filter(None, arr))
# a = boyer(txt, pat)  
# print(a)