def KMP(txt, pat):
    m = len(pat) 
    n = len(txt) 
    prefthatsuf = [0 for i in range(m)]
    countPrefSuf(pat, prefthatsuf) 
    i = 0
    j = 0
    while i < n: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        if j == m: 
            return True 
        elif i < n and pat[j] != txt[i]: 
            if j != 0: 
                j = prefthatsuf[j-1] 
            else: 
                i += 1
    return False

def countPrefSuf(pat, prefthatsuf): 
    idx = 0
    prefthatsuf[0] = 0 
    i = 1
    while i < len(pat): 
        if pat[i]== pat[idx]: 
            idx += 1
            prefthatsuf[i] = idx
            i += 1
        else: 
            if idx != 0: 
                idx = prefthatsuf[idx-1] 
            else: 
                prefthatsuf[i] = 0
                i += 1
  
# txt = "Liputan6.com, Jakarta - Top 3 Berita Hari Ini tentang durian Musang King yang kini banting harga"
# pat = "Musang"
# # a_list = nltk.tokenize.sent_tokenize(txt)
# # print(a_list)
# print(KMP(txt, pat))