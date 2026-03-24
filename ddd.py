'''
#2.uzdevums

vardi=[] #vardi=list()

datne=open("vardi (2).txt","r",encoding="utf-8")

dati=datne.read()
print(dati)
print(type(dati))

#vardi=dati.spli(",")
vardi.sort()
for i in dati.split(","):
     if i.startswith("r"):
     print(i)
     with open("r.txt","a",encoding="utf-8") as f:
         f.write(i+",")
datne.close()
'''

#3.uzdevums
temp=[]
datne=open("temperaturas.txt","r",encoding="utf-8")
dati=datne.read()#rezultāts ir virkne.
datne.close()
temp=dati.split(", ")
print(temp[1],temp[12],temp[22])
print(f"{float(temp[8])*9/5+32} {float(temp[12])*9/5+32} {float(temp[14])*9/5+32}")
print(f"vidējā{(float(temp[0])+
float(temp[6])+
float(temp[12])+
float(temp[18]))/4}")






