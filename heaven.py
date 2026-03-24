'''
import json
mp=["matematika", "sports" , "bioloģija" ,"vesture", "latviešu valoda"]

datne=open("macibuprieksmeti.json","w")
json.load(datne)
print(mp)
datne.close()
'''

'''
import json
f=open("uzd.json","a")
skaitli=[1,2,3,4,1]

json.dump(skaitli,f)
f.close()
#f=open("uzd.json","w")
#dati=json.load(f)
#print(dati)
'''

'''
import re
text="mans telefona nr.11037183"

atbilde=re.search(r"\d{8}",text)
print(atbilde.group())#veidojas ne saraksts.

atbilde2=re.findall(r"\d{8}",text)
print(atbilde2)#"find all" veidojas saraksts.

atbilde3=re.findall(r"\d{8}",text)
#print(atbilde3)

atbilde4=re.search(r"\btelefona",text)
print(atbilde4.group())#atradīs vārdu "telefona".

atbilde5=re.sub(r"\b\d{8}\b","@@",text)#replace ciparus ar jeb kādu simbolu.
print(atbilde5)

#fails=open("re.txt",encoding="utf-8")#atvērt
info=fails.read()#paradīt ka tā ir virkne
fails.close()#aizvērt

atbilde8=re.findall(r"\blaimests|bezmaksas|bankas konts\b",info,re.IGNORECASE)
print(atbilde8)
'''

'''
import re
with open("klienti.txt","r",encoding="utf-8") as fails:
    dati=fails.read()#vrikne

epasti=re.findall(r"w+@\w+\.\w+",dati)
print(epasti)#saraksts

telefoni=re.findall(r"\d{8}",dati)
print(telefoni)#saraksti

aizvietots=re.sub(r"\d{8}","✆",dati)
print(aizvietots)

datne=open("klienti_anon.txt","w",encoding="utf-8")
datne.write(aizvietots)
datne.close()
'''







