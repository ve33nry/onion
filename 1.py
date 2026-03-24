
'''
def funkcija(): #definēju tukšu funkciju
    pass
funkcija ()#izsaucu funkciju
print(funkcija()) #izvadu funkciju
'''

'''
a=12
b=2
def saskaitisana(a,b):
 return a+b

saskaitisana(a,b)
print(saskaitisana(a,b))

def atnemsana(a, c=13):
 print(a-c)

atnemsana(a)

def reizinasana (a,b):
 return a*b

print(reizinasana (a,b))

def dalisana(a,b):
 print(a/b)

dalisana(a,b)

izvele=input("izvēlies +, -, *, /")
if izvele=="+":
 print(saskaitisana(a,b))
elif izvele=="-":
 atnemsana(a)
elif izvele=="*":
 print(reizinasana(a,b))
elif izvele=="/":
 dalisana(a,b)
else:
 print("kļūda")
'''

'''
sk=int(input("sk= "))
def skaitlis(sk):
   if sk %2==0:
     print("pāraskaitlis")
   else:
     print("nepāra")

skaitlis(sk)
'''

'''
m=int(input("masa= "))
c=300000000

def Einstein(m,c):
 E=m*c**2
 print(E,"džouli")

Einstein(m,c)
'''

'''
maltites_izmaksas=float(input("cik jasamaksā?"))
procenti=int(input("10, 15, citi%"))



def dzeramnauda(maltites_izmaksas,procenti):
  summa=maltites_izmaksas*procenti/100
  print(summa,"eiro")

dzeramnauda(maltites_izmaksas,procenti)
'''

