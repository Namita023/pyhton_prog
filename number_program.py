#prime number
def is_prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
#print(is_prime(17))

#composite number
def is_composite(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount>2
#print(is_composite(20))

#Perfect number
def sum_fact(num,dsum=0):
    for fa in range(1,num):
        if num%fa==0:
            dsum+=fa
    return dsum
def is_prime(num):
    return num==sum_fact(num)
#print(is_prime(6))

#Pronic number
def is_pronic(num,n=0):
    while n*(n+1)<num:
        n+=1
    return num==n*(n+1)
#print(is_pronic(12))

#Sunny number
def is_sunny(num,n=0):
    while (num+1)>n*n:
        n+=1
    return (num+1)==n*n
#print(is_sunny(15))

#Niven number
def is_niven(num,dsum=0):
    while num!=0:
        dsum+=num%10
        num//=10
    return num%dsum==0
#print(is_niven(4536))

#Spy number
def sum_dig(num,dsum=0):
    while num!=0:
        dsum+=num%10
        num//=10
    return dsum
def prod_dig(num,prod=1):
    while(num!=0):
        prod*=num%10
        num//=10
    return prod
def is_spy(num):
    return sum_dig(num)==prod_dig(num)
#print(is_spy(123))

#Palinedrome number
def reverse(num,rev=0):
    while num!=0:
        rev=rev*10 + num%10
        num//=10
    return rev
def is_palinedrome(num):
    return num==reverse(num)
#print(is_palinedrome(232))

#PalyPrime number
def prime(num,dsum=0):
    while num!=0:
        dsum+=num%10
        num//=10
    return dsum==2
def reverse(num,rev=0):
    while num!=0:
        rev=rev*10 + num%10
        num//=10
    return rev
def is_palinedrome(num):
    return num==reverse(num)
def is_palyprime(num):
    return prime(num) and is_palinedrome(num)
#print(is_palyprime(11))

#emirp number
def reverse(num,rev=0):
    while num!=0:
        rev=rev*10+num%10
        num//=10
        return rev
def palinedrome(num):
    return num!=reverse(num)
def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
def rev_prime(rev,fcount=0):
    for fa in range(1,rev+1):
        if rev%fa==0:
            fcount+=1
    return fcount==2
def is_emrip(num):
    return palinedrome(num) and prime(num) and rev_prime(num)
#print(is_emrip(17))
#print()

#armstrong number
def dig_sum(num,s=0):
    count= len(str(num))
    while num!=0:
        s+=(num%10)**count
        num//=10
    return s
def is_armstrong(num):
    return num==dig_sum(num)

#print(is_armstrong(407))

#disarium number
def digit_sum(num,dsum=0):
    count=len(str(num))
    while num!=0:
        dsum+=(num%10)**count
        num//=10
        count-=1
    return dsum
def is_disarium(num):
    return num==digit_sum(num)
#print(is_disarium(135))

#strong/special number
def fact(num,dsum=0):
    while num!=0:
        factorial=1
        ld=(num%10)
        for fa in range(1,ld+1):
            factorial*=fa
        dsum+=factorial
        num//=10
    return dsum
def is_strong(num):
    return num==fact(num)
#print(is_strong(145))

#happy number
def is_happy(num):
    while num>=10:
        num= dig_sum(num)
    return num==1
def dig_sum(num,dsum=0):
    while num!=0:
        dsum+=(num%10)**2
        num//=10
    return dsum
#print(is_happy(44))

#Automorphic number
def is_automorphic(num):
    return num==last_dig(num)

def last_dig(n):
    num=n**2
    ld=num%(10**len(str(n)))
    return ld

#print(is_automorphic(25))

#trimorphic number
def is_trimorphic(num):
    return num==last_digit(num)

def last_digit(n):
    num=n**3
    ld=num%(10**len(str(n)))
    return ld

#print(is_trimorphic(25))

#neon number
def dig_sum(num,dsum=0):
    n=num**2
    while n!=0:
        dsum+=(n%10)
        n//=10
    return dsum

def is_neon(num):
    return num==dig_sum(num)

# print(is_neon(9))

#evil/odious number
def reminder(num,count=0):
    while num!=0:
        rem=num%2
        count+=rem
        num//=2
    return count

def is_evil(num):
    return reminder(num)%2==0

# print(is_evil(89))

#tech number
def is_tech(num):
    n1=num//(10**(len(str(num))//2))
    n2=num%(10**(len(str(num))//2))
    return (len(str(num))%2==0) and num==(n1+n2)**2
