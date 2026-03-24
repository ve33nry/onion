'''
#Smile face
zime=input("izvēlies :), :( ")
#def funkciju convert
def convert(zime):
    if zime==":)":
        print("🍌")
    elif zime==(":("):
        print("🐟")
    elif zime==("˙𐃷˙"):
        print("📈")
    elif zime==("★"):
        print("🎥")
    elif zime==("HHHH"):
        print("🌭")
    else:
          print("nezināmā zīme")
convert(zime)
'''

'''
for x  in range (10): #No 1 līdz 10 neieskaitot
    print(x+1)
'''
'''
for x in range(20,0,-1):
    print(x)
'''

'''
for x in range(1,10):
    y=x**2+3*x-2
    print(f'ja x={x}, tad y={y}')
'''

'''
import random
x=random.randint(0,8)
print(x)
'''

'''
#a
#biblioteka brīvi ģenerēta skaitļa izvelei
import random
m=int(input("m: "))
for i in range(m):
    sk=random.randint(0, 60)
    print(f'{i+1}. {sk}')


#b
for i in range(m,0-1, -1):
    sk=random.randint(0, 60)
    print(f'{i}. {sk}')
'''

'''
#skaitļu skaits
c=int(input("skaitļu skaits: "))
summa=0
for k in range(c):
    sk=int(input("sk: "))
    summa+=sk
    print(summa)
print("sum=",summa)
'''
import math  # importēj7u math bibliotēku

'''
for n in range(7,13):
    print(math.pow(n,2))
    #print(n**2)#kāpināšanas zīme
'''
'''
#kvadrātsaknes
import math
for k in range (27,17,-1):
    print(math.sqrt(k))
'''

'''
for i in range(1,50):
    if i%3==0 or i%5==0:
        print(i)
    else:
        print("nedalās 3 vai 5")
'''

'''
n=int(input("n: "))
if n>1:
       for i in range(1,n):
         print(i,i**2)
       else:
           for i in range(n,1,):
               print(i,i**2)
'''

'''
for x in range(1,20):
    if x%2==0:
        continue
    else:
        print(x,"ir nepāra")
'''

'''
x=int(input("x: "))#skaitļu skaits
sum=0
for i in range(x):
     sk=int(input("sk: "))
     if sk>=0:
         sum+=sk
     else:
         break
print("pozitīvo skaitļu summa",sum)

x=int(input("x: "))
for i in range(x):
    sk=int(input("sk: "))
    if sk%3>0 or sk%5>0:
        break

while True:#bezgalīgais cikls
sk=int(input("sk= "))
if sk%3==0 or sk%5==0:
break
elif sk%4==0:
continue
else:
print("nedalas ar 3, 4 vai 5")


k=int(input("k= "))
n=int(input("n= "))

while k<=n:
print(n)
k+=1


k=int(input("k= "))
n=int(input("n= "))
if k>n:
while k>n:
print(k)
elif n>k:
while n>k:
print(n)
else:
print(k=n)


m=int(input("m= "))
s=0
while s sk=random.randint(0,20)
print(sk)
s+=1
'''

'''
#1lats=1,42eur
lats=1.42
latu_skaits=float(input("cik daudz latu?"))
def pelmenis(lats, latu_skaits):
    print(f'{lats*latu_skaits:.2f} eur.')

pelmenis(lats,latu_skaits)
'''

'''
pepsa = 50  # 1 pudele pepesa
summa = 0


def automats(pepsa, summa):
    nauda=int(input("naudas cik"))
    while summa<=pepsa:
        if nauda==20 or nauda==10 or nauda==5:
            # cik maksāt
            summa+=nauda
            print(f'iemaksāts:{summa}')
        if pepsa-summa>= 0:

            # cik vēl jaiemaksa
            print(f'vēl terūkst{pepsa - nauda}centu')
        else:
            print(f'atlikums{summa - pepsa}centu')
    else:
        print("automāts ne")
automats(pepsa,summa)
'''

'''
#aprakstīsim 2 virknes
v1=input("virkne1: ")
v2=input("virkne2: ")
#konkatē 2 virknes
v3=v1+v2
print(v3)
v1+=v2
print(v1)

v4=v1*8
print(v4)
'''
'''

print(a,b,c)
'''


'''
vards=input("ievadi vārdu").capitalize()
print(vards)
'''

'''
s1="abrakadabra"
s1=s1.replace("a", "o")
print(s1.find("o"))#atrod pirmo o, izvada pozīciju
print(s1.isalpha())#burtu pārbaude
print(s1.isdigit())#ciparu pārbaude
print(s1.isalnum())#visa pārbaude

s1=input("ievadi virkni: ")
print(s1.replace(" ","..."))
print(s1.find("k", -1))
print(s1.center(len(s1)+10,"@"))
print(ord(s1[0]))
'''

'''
x1=input("ievadi virkni: ")
x2=""
for a in range(len(x1)):
    print(ord(x1[a]))
    x2+=str(ord(x1[a]))+" "

x=input("ievadi virkni: ")
print(len(x))
#2.uzdevums
for y in range(len(x)):
    print(x[y])
#3.uzdevums
print(x[0],x[-1])


#4.uzdevums
k=input("ievadi virkni: ")
print(x[0]+"."+k[0]+".")
#5.uzdevums
#print("n"x,upper())

#6.uzdevums
print(k.lower())
print(k.casefold())
'''

'''
#7.uzdevums
#Camelcase
c=input("ievadi virkni: ")
b=input("ievadi virkni: ")
print(c.casefold()+b.capitalize())
print(b.lower()+"_",c.lower())
#8.uzdevums
for i in range(len(c)):
    if c[i]=="a"or c[i]=="e"or c[i]=="i"or c[i]=="u"or c[i]=="o":
        b+=""
    else:
        b+=c[i]
print(b)
'''

'''
#9.uzdevums
M=input("ievadi virkni: ")
print(M.replace("", "..."))
print(M)
'''

'''
#1.uzdevums
v="thequickbrownfoxjumpsoverthelazydog"
print(v[::3])#izvada katru trešo simbolu
print(v[::-1])#virkne preteja virziena
print(v[::-2])#izvada preteja virziena katru 2 simbolu
print(v.count("the"))
print(v.replace("a","d"))
'''

'''
#2.uzdevums
def nosaukums(v):
 v=input("ievadi virkni: ")
def garums(v):
   if len(v)<5:
     print(v)
   else:
     print(v[0],v[1],v[-2],v[-1])
garums(v)
'''

'''
#3.uzdevums
v=input("ievadi virkni: ")
f=input("ievadi virkni: ")
print(len(v))
print(len(f))
v3=''
for i in range(len(v)):
    if len(v)<len(f):
        print(v[i])
    elif len(v)<len(f):
        print(f[i])
    else:print("virknes vienādas")
'''


'''
#1.uzdevums
v=input("ievadi virkni: ")
print(v[0],v[-1])
print(len(v))

'''

'''
#2.uzdevums
x=input("ievadi virkni: ")
print(x," ",x)
#variants 2
x+=" "+x     #pie virknes pieskaitīt klāt atstarpi un dubultot virkni.
print(x)
print(x.replace(x[0:2],"%")+x[2::]
#2.variants
x[0]=%
'''






'''
#3.uzdevums
x=input("ievadi virkni: ")
print(x[::-1])
print(x[::-2])

'''

'''
#4.uzdevums
x=input("ievadi virkni: ")
print(x.count("e"))
'''

'''
#5.uzdevums
x=input("ievadi virkni: ")
print(x[7:12])

'''

'''
#6.uzdevums
x=("abrakadabra")
print(x.find("a"))
print(x.replace("a","k"))



#7.uzdevums
x=input("x= ")
burts=input("burts= ")

if burts in x:
    print(ord(burts))
'''

'''
#8.uzdevums
kripto=' '
x=input("ievadi virkni: ")
for i in range(len(x)):
    x=bin(ord(x[i]))
    kripto+=x.replace("b", "")+' '

print(kripto)
'''

x=("brbrpatapim")
print(x.find("A"))
print(x.replace("A","S"))
print(x.find("a"))
print(x.replace("a","K"))
print(x.find("B"))
print(x.replace("B","x"))
print(x.find("b"))
print(x.replace("b","y"))
print(x.find("C"))
print(x.replace("C","P"))
print(x.find("c"))
print(x.replace("c","!"))