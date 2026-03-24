'''
import re
with open("klienti.txt","r",encoding="utf-8")as fails:
    dati=fails.read()#vrikne

epasti=re.findall(r"w+@\w+\.\w+",dati)
print(epasti)#saraksts
print(len(epasti))

telefoni=re.findall(r"\d{8}",dati)
print(telefoni)#saraksti

aizvietots=re.sub(r"\d{8}","✆",dati)
print(aizvietots)#virkne

datne=open("klienti_anon.txt","w",encoding="utf-8")
datne.write(aizvietots)
datne.close()
'''


