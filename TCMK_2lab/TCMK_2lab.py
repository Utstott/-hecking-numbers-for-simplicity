from math import gcd
import random
def Jacobi(a, n):
    s = 1
    while True:
        if n < 1: raise ValueError("Ошибка: " + str(n))
        if n & 1 == 0: raise ValueError("Ошибка")
        if n == 1: return s
        a = a % n
        if a == 0: return 0
        if a == 1: return s
        
        if a & 1 == 0:
            if n % 8 in (3, 5):
                s = -s
            a >>= 1
            continue
        
        if a % 4 == 3 and n % 4 == 3:
            s = -s
        
        a, n = n, a
    return

def Algoritm_Ferma(number):
     global Ferma_base
     Ferma_base=random.randint(2,number-2)
     Result=pow(Ferma_base,number-1,number)
     if Result!=1:
        return -1
     else:
         return 0

def Algoritm_Sol_Sh(number):
    global Ferma_base
    Ferma_base=random.randint(2,number-2)
    Result=pow(Ferma_base,(number-1)>>1,number)
   
    d = gcd(number, Ferma_base)
    if  Result!=1 and Result!=number-1:
        print("Нарушено условие: Result != 1 и Result != number-1")
        return -1
    Symbol=Jacobi(Ferma_base,number)
    if Result!= Symbol % number:
        print("Нарушено условие: символ Якоби не равен Result" )
        return -1
    else:
        return 0


def Algoritm_Rob_Mill(number):
     global Ferma_base
     Ferma_base=random.randint(2,number-2)
    
     s, r = 0, number - 1
     while r % 2 == 0:
        s, r = s + 1, r>>1

     Result=pow(Ferma_base,r,number)
     if Result !=1 and  Result!=number-1:
    
         j=1
         for j in range(s-1):
            Result=pow(Result,2,number)
            if Result==number-1:
                 break
        
            if Result==1:
                print("Нарушено условие: Result=1" )
                return -1
        
        
         if Result!=number-1:
               print("Нарушено условие: Result!=number-1" )
               return -1
  
     return 0


data = []
with open("text.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
a =data[0][0]
b = data[1][0]
c=data[2][0]
d=data[3][0]
Base_arr = [0, 0, 0, 0, 0]
if a<5:
    print("Число меньше 5:" + str(a))
    a=-1
   
if b<5:
    print("Число меньше 5:" + str(b))
    b=-1

if c<5:
    print("Число меньше 5:" + str(c))
    c=-1
if a%2==0:
    print("Четное число:" + str(a))
    a=-1
if b%2==0:
    print("Четное число:" + str(b))
    b=-1
if c%2==0:
    print("Четное число:" + str(c))
    c=-1

if a!=-1:
    flag=0
    print("Тест Ферма для " +str(a) +":\n")
    for i in range(5):
        Res=Algoritm_Ferma(a)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    flag=0
    print("Тест Соловэя-Штрассена для:" +str(a)+":\n")
    for i in range(5):
        Res=Algoritm_Sol_Sh(a)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    print("Тест Рабина-Миллера для:" +str(a)+":\n")
    flag=0
    for i in range(5):
        Res=Algoritm_Rob_Mill(a)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
     
if b!=-1:
    flag=0
    print("Тест Ферма для " +str(b) +":\n")
    
    for i in range(5):
        Res=Algoritm_Ferma(b)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    flag=0
    print("Тест Соловэя-Штрассена для:" +str(b)+":\n")
    for i in range(5):
        Res=Algoritm_Sol_Sh(b)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    print("Тест Рабина-Миллера для:" +str(b)+":\n")
    flag=0
    for i in range(5):
        Res=Algoritm_Rob_Mill(b)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
if c!=-1:
    flag=0
    print("Тест Ферма для " +str(c) +":\n")
    for i in range(5):
        Res=Algoritm_Ferma(c)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    flag=0
    print("Тест Соловэя-Штрассена для:" +str(c)+":\n")
    for i in range(5):
        Res=Algoritm_Sol_Sh(c)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    print("Тест Рабина-Миллера для:" +str(c)+":\n")
    flag=0
    for i in range(5):
        Res=Algoritm_Rob_Mill(c)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
if d!=-1:
    flag=0
    print("Тест Ферма для " +str(d) +":\n")
    for i in range(5):
        Res=Algoritm_Ferma(d)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    flag=0
    print("Тест Соловэя-Штрассена для:" +str(d)+":\n")
    for i in range(5):
        Res=Algoritm_Sol_Sh(d)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
    print("Тест Рабина-Миллера для:" +str(d)+":\n")
    flag=0
    for i in range(5):
        Res=Algoritm_Rob_Mill(d)
        if Res==0:   
            Base_arr[i]=Ferma_base
        else:
            print("Составное число.Основание:" + str(Ferma_base) + "\n")
            flag=1
            break
    if flag==0:
        print("Число, возможно, простое. Основения: " +str(Base_arr[0])+","+str(Base_arr[1])+","+str(Base_arr[2])+","+str(Base_arr[3])+","+str(Base_arr[4])+"\n")
