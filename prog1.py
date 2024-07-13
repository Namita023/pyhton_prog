#WAP to print sum of prime digits in given number
num= 934093631
sum= 0
while num!= 0:
    ld = num%10
    fcount=0
    for fa in range(1,ld+1):
        if (ld % fa==0):
            fcount+=1
    if fcount==2:
        sum+=fa
    num//=10
print(sum)
print("\n")

#WAP to print prime numbers from 23 to 43

for num1 in range(23,44):
    fcount=0
    for n in range(1,num1+1):
        if num1%n==0:
            fcount+=1
    if fcount==2:
        print(num1)
print("\n")

#WAP to print prime numbers from 43 to 23

for num in range(43,22,-1):
    fcount=0
    for fa in range(1, num+1):
        if num%fa==0:
            fcount+=1
    if fcount==2:
        print(num)
print("\n")

#WAP to print higest prime number from 10 to 50

highest=0
for num in range(10,51):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    if (fcount==2 and num>highest):
        highest=num
print(highest)
print()

#WAP to print alternate prime numbers from 1 to 30

sum=0
for num in range(1,31):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
        sum+=1
    if (fcount==2 and sum%2==0):
        print(num)
print('\n')

#WAP to print all the three digit prime number

for num in range(100,1000):
    fcount=0
    for f in range(1,num+1):
        if num%f==0:
            fcount+=1
    if (fcount==2):
        print(num,end=", ")

#WAP to print2 digit PalyPrime number

for num in range(10,100):
    copy=num
    rev=fcount=0
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num//=10
    for fa in range(1,copy+1):
        if copy%fa==0:
            fcount+=1
    if (copy==rev and fcount==2):
        print(copy)                                                            

#WAP to print 3 digit armstrong number
        
for num in range(100,1000):
    copy=num
    count=len(str(num))
    dsum=0
    while num!=0:
        ld=num%10
        dsum+=ld**count
        num//=10
    if copy==dsum:
        print(copy)
print()

#WAP to 3 digit emirp number

for num in range(100,1000):
    copy=num
    rev=0
    fcount1=fcount2=0
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num//=10
    for fa in range(1,copy+1):
        if(copy%fa==0):
            fcount1+=1
    for fa in range(1,rev+1):   
        if(rev%fa==0):
            fcount2+=1
    if(copy!=rev and fcount1==2 and fcount2==2):
        print(copy)
print()

for num in range(50,9,-1):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    if(fcount==2):
        print(num)
        break
print()
