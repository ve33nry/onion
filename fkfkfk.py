
"""""""""
#3.uzdevums
skaitlis=float(input("uzmini skaitli:"))
if skaitlis==56:
    print("uzvarēji!")
else:
    print("neizdevās!")

#4.uzdevums
a=input ("vai ir piens jā/nē?")
if a=="jā" or a=="ja":
    print("pārslas ar pienu")
elif a=="ne" or a=="nē":
     print ("sviestmaize")
else:
    print("sidi golodni")
#5.uzdevums
mac_pr=input("izvēlies ķimija / sports / angļu valoda / mūzika ")
if mac_pr=="ķīmija":
    print("tev patīk ķīmija")
elif mac_pr=="angļu valoda":
    print("tev patīk angļu valoda")
elif mac_pr=="sports":
    print("tev patīk sports")
elif mac_pr=="mūzika":
    print("tev patīk mūzika")
else:
    print("neuch")
#6.uzdevums
budzets=float(input("ievadi budžetu:"))
if budzets<=0:
    print("vēl jakrāj")
elif budzets<500 and budzets>0:
    print("ceļo uz BULGĀRIJU")
elif budzets>=500 and budzets<1000:
    print("ceļo uz FRANCIJU")
else:
    print("Idk")
#7.uzdevums
Garastavoklis=input("garastāvoklis labs/slikts?")
if Garastavoklis=="labs":
    print("Klausāmies iecienīto mūzkiu")
if Garastavoklis=="slikts":
      print("Klausāmies relaksējušo mūzkiu")
else:print("Klausies ko gribi")
#8.uzd
augs=input("augs izskatās vesels/slims")
if augs=="vesels":
    print("rāvē nezāli")
elif augs=="slims":
    print("jālaista")
else:
    print("lai nomirst jau")
#9.uzdevums
nauda=float(input("cik ir naudas?"))
pirkums=float(input("cik maksā pirkums?"))
if nauda>=pirkums:
    print(f"preci var nopirkt, paliks pāri {nauda-pirkums} eiro.")
elif pirkums>nauda:
    print(f"Vēl jaiekrāj {pirkums-nauda}")
"""""""""""
'''
#1.uzdevums
import math
x=int(input("ievadi brāļū skaitu"))
y=int(input("ievadi konfekšu skaitu"))
#Jāaprēķina, cik konfekšu būs katram...
c=y/x
#print(round(c))
#noapaļošana ar iztrūkumu
print(math.floor(c))

m=y%x
print(m)
'''
'''
#2.uzdevums
import math
c=300000000
m=float(input("ievadi masu: "))
E=m*math.pow(c,2)
#E=m*c**2
print("E=",E)
print("E=",E,"džouļi")
'''
'''
x,y,z=input("ievadi izteiksmi:").split()
x=int(x)
z=int(z)
#darbības +,-,*,/
if y=="+":
    print(f"skaitļu summa ir {(x+z):.1f}")
elif y =="-":
    print(f"skaitļu summa ir {(x-z):.1f}")
elif y =="*":
    print(f"skaitļu summa ir {(x*z):.1f}")
elif y =="/":
    print(f"skaitļu summa ir {(x/z):.1f}")
else:
    print("nezināmā zīme")
'''
'''
for k in range (55,33,-3):
    print(k)
'''

'''
#aprēķini 8 skaitļu summu
sum=0
for n in  range(8):
    sk=int(input("sk= "))
    sum+=sk #sum+sk
    print(sum)
'''

'''
import math
for x in range(1,10):
    y=math.pow(x,2)+3*x-2
    print(f"Ja x={x}, tad y={y}")
'''

'''
sak_vert=2
while sak_vert<10:
    print(sak_vert)
'''

'''
#pēc specifikācijas ievadu veselos sk...
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
#veikt aprēķinu pēc apraksta...
x=2*a*b
y=5*c
t=x+y

#pēc pasūtītāja prasības izvadām
print("t=",t)
#pēc uzdevuma specifikācijas mērvienības nav nepieciešamas
'''

'''
#2.uzdevums
x=int(input("x: "))
#mērvienību nav, datu tipu noteica pasūtītājs
#aprēķins
if x<=3:
    y=2*x-6
else:
    y=x+5
#pēc psūtītaja specifikācijas izvedam kā formatēto virkni...
print(f"y={y}")
'''

'''
#3.uzdevums
#pēc uzdevuma specifikācijas pieprasām ievadīt veselu skaitli...
skaitlis=int(input("choose a number from 1 to 5 and get your silly disease :333 "))
#mērvienības nav nepieciešamas...
#aprēķins pēc uzdevuma specifīkācijas...
if skaitlis==1:
    print("diabetes")
elif skaitlis == 2:
    print("covid-19")
elif skaitlis == 3:
    print("black plague")
elif skaitlis == 4:
    print("lung cancer")
elif skaitlis == 5:
    print("cold")
else:
    print("everythings fine ig")
'''

'''
skaits=int(input("kreklu skaits= "))
apdruka=input("Teksts/Zime/Foto/")
piegade=input("Vai nepieciešama piegāde? Jā/Nē")

if apdruka=="Teksts":
    cena=5
elif apdruka=="zīme":
    cena=7
elif apdruka=="foto":
    cena=20

else:
    print("pārbaudi ievadi!")

#aprēķins par krekliem
kopsumma=input(skaits*cena)

#piegade ? atlaide?
if kopsumma<50:
    piegade_e=15
    atlaide=0
elif kopsumma>=50:
    atlaide=0
    piegade_e=0
elif kopsumma>100:
    piegade_e=0
    atlaide=0.05
else:
    print("kļūda")
if piegade=="Jā":
    izmaksas=kopsumma+piegade_e+atlaide
elif piegade=="Nē":
    izmaksas=kopsumma+atlaide
else:
    print("kļūda emmm")
if piegade=="Jā":
    izmaksas=kopsumma+piegade_e-atlaide
elif piegade=="Nē":
    izmaksas=kopsumma-atlaide
else:
    print("kļūda")
print(f"krekli ar {apdruka} un {izmaksas} eiro. ")
'''

'''
#1.uzdevums
import math
linoleja_p=int(input("linoleja platums= "))
cena=float(input("linoleja cena= "))
telpas_p=int(input("telpas platums"))
telpas_g=float(input("telpas garums"))
telpas_l=telpas_g*telpas_p
izmaksas=telpas_l*cena
print(f"linoleja ieklāšanas cena ir {izmaksas}")
'''

'''
#2.uzdevums
import math
#Ievadu mainīgos
Ind_klienti=int(input("cilvēku skaits= "))
cena=float(input("laikraksta cena= "))
laikraksts=int(input("laikrakstu nedēļā= "))
laikrakstu_cena=float(input("laikraksta cena= "))
#Aprēķini
izmaksas1=laikraksts/laikrakstu_cena
izmaksas2=cena/Ind_klienti
print(f"individuālo laikrakstu cena ir {izmaksas2}")
print(f"Laikrakstu cena ir {izmaksas1}")
if izmaksas1>izmaksas2:
    print("focus on laikraksti")
elif izmaksas2>izmaksas1:
    print("focus on individuals")
else:
    print("strādā tādā pašā tempā")
'''

#3.uzdevums
import math
#Mainīgie
d_p=int(input("dzēšamo pildspalvu skaits= "))
g_p=int(input("Gēlija pildspalvu skaits= "))
t_p=int(input("Tintes pildspalvu skaits= "))
dp_c=float(input("dzēšamo pildspalvu cena=  "))
gp_c=float(input("Gēlija pildspalvu cena=  "))
tp_c=float(input("tintes pildspalvu cena=  "))
#izmaksas aprēķini
izmaksa1=d_p+g_p+t_p
izmaksas2=dp_c+gp_c+tp_c
print(f"pildspalvu skaits ir {izmaksa1}")
print(f"pildspalvu cena ir {izmaksas2} centi")
