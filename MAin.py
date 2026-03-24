
datne=open("iepirkumi.txt","a",encoding="utf-8")
preces=(input("iveadi 6 preces= "))
grozs=[]
papildus=["piens","siers","kefīrs"]
grozs.append(preces)
grozs.append(papildus)
print(grozs)
grozs.sort()
datne.close()


