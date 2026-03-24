'''
#Sasraksti
t1=[]
t2=list()
t3=[3,4,5,6,7]#dots skaitļu saraksts
t4=['g','o','i','d','a']#dots virkņu saraksts
t5=[1,2.45,'Maija']
t6=[t3,t4,t5]

print(t3[0], t3[-1])
print(t3[1:3])
print(t4[0::])#sākotnēja pozicija un līdz galam...
print(t4[::-1])#pretējā virzienā
print(t3[::2])#no saraksta sākuma līdz beigām katru otro.
print(t4[::-2])#katrs 2 no citas puses.

t3.sort(reverse=True)#sakārto sarakstu pretējā virzienā
t4.sort(reverse=True)
t4.reverse()
print(t3)
print(t4)
'''

'''
sk_s=[]
for i in range(3):
    sk=int(input("sk= "))
    #sk_s.append(sk)#variants 1
    sk_s.insert(i,sk)#variants 2
print(sk_s)
'''

'''
t3=[3,4,5,6,7]
import random #random bibliotēka
sk_s=[]
for i in range(3):
    sk=random.randint(1, 10) #ģenerē skaitļus na random
    sk_s.insert(i,sk)
print(sk_s)
#min
print("min=",min(sk_s))
#max
print("max=",max(sk_s))
#sum
print("sum=",sum(sk_s))
#vidējais
("vidējais=",sum(sk_s)/len(sk_s))

#count
print(t3.count(3)) #skaita vērtibas ir sarakstā
#pop
sk_s.pop()#nodzēš pēdējo elementu
print(sk_s)
'''

'''
#Saskaitīt sarakstus vienā sarakstā.
x=[1,2,3,4,5]
y=[5,6,7,8,9]
z=x+y #kura ir pirmā virkne,tā arī parādās.
print(type(z),z)
print(x*3) #viena virkne atkārtojas 3 reizes.
for i in z:#pārlasa saraksta elementus.
    print("elements",i)#izdrukā sarakstu stabiņā.
'''
'''
celasoma=[["cepure","zeķes","šalle"],["soma","krekli"]]
print(type(celasoma),celasoma)
#divas kvadrātiekavas veido sarakstu.
print(celasoma[0])
for i in celasoma [0]:
    print(i)
    print(celasoma[0][-1])
    #Izvada stabiņu ar pirmo sarakstu.
print(celasoma[1])
for i in celasoma[1]:
    print(i)
    print(celasoma[1][0])
 '''

'''
x=["galva",8,6,4.5,27]
x.insert(len(x),"vēl viens")
#x.append("vēl viens")#Strādā.
#insert un extend strādā ar diviem argumentiem, te ir tikai viens.
#extend strādā ar pašu sarakstu.
print(x)
 '''

'''
x=["Zils","Zeme","Pildspalva","Grāmata","Zaļš","Jūra","8"]
x.insert(len)(x),"saule")
x.insert(3,"mākonis")
print(x)
for i in x[1]:
    print(i)
'''

'''
c1=["dators","robots","planšete",]
c1.insert(0,"hibrīds")
c1.pop()
print(c1[::-1])

datne=open("uzd.txt","w",encoding="utf-8")#1.
#datne.write(str(c1))
for i in c1:
    datne.write(i+"\n")
datne.close()




with open("uzd1.txt","a",encoding="utf-8") as datne:#2.
    for i in c1:
        datne.write(i+"\n")
    datne.close()
'''

'''
nedela=["pirmdiena","otrdiena","trešdiena","ceturdiena","piketdiena","sestdiena","svētdiena"]
x=open("nedela.txt","a",encoding="utf-8")
#x.write(str(nedela))#str pārveido par virkni.

for i in nedela:
    x.write(i+" ")
x.close()


c=open("nedela.txt","r+",encoding="utf-8")
dati=c.read()
saraksts2=[]
info=dati.split()
for i in info:
    saraksts2.append(i)
print(saraksts2)
'''

'''
x=[]
k=5
datne=open("ievade.txt","w",encoding="utf-8")
for i in range(k):
    sk=int(input("sk="))
    x.append(sk)
    datne.write(str(x)+" ")
datne.close()
print(f"summa{sum(x)}")
print(f"min{min(x)}")
print(f"max{max(x)}")
print(f"vid{sum(x)/k}")

reizin=1
    #skaitļu reizinājums
for i in x:
    reizin*=i

print(reizin)
'''

'''
#5.uzdevums
datne=open("skaitli.txt","w",encoding="utf-8")
sk=[1,2,3,4,5]
x=[]
for i in range(5):
 sk=random.randit(a, b)
print(f"summa{sum(sk)}")
print(f"min{min(sk)}")
print(f"max{max(sk)}")
print(f"vid{sum(sk)/5}")
datne.close()
'''

'''
#6.uzdevums
import random
x=[]
for i in range(3):
    sk=random.randint(1, 10)
    x.insert(i,sk)
datne=open("apvienosana.txt","w",encoding="utf-8")
v=['Zils','Zeme','Pildspalva','Grāmata','Zaļš','Jūra','8']
datne.write(str(x))
'''

'''
import random
sk=[-24, -10, 2, 6]
skaitli=[]
for i in range(7):
    sk1=random.randint(-16,8)
    skaitli.insert(i,sk)
print(skaitli)
#sarakstu apvienošana
#skaitli+=sk
#skaitli.extend(sk) print(skaitli)
skaitli.insert(0,sk1)
print(skaitli)
skaitli.append(-8)
skaitli.insert(2,-18)
print(skaitli)
skaitli.remove(skaitli[5])
print(skaitli)
datne=open("skatili2.txt","w", encoding="utf-8")
datne.write(str(skaitli))
datne.close()
print(f"min={min(skaitli)},max={max(skaitli)},vid={sum(skaitli)/len(skaitli)}")
'''

'''
fails.open("vardi.txt","r",encoding="utf-8")
dati=fails.read().split(", ")
dati.sort()
print(type(dati))
for i in dati:
    if i.startwith("R")==True:
        print(i)
'''































