#for loop
d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(f'{key} = {value}')

print()
L=[10,20,30]
for num in L:
    print(num*100)

print()

s={'abc',10,20,True,1,'abc'}
for ch in s:
    print(ch)

print()
#for else loop
S="python"
for ch in S:
    print(ch)
else:
    print("end")

print()
#Print the first 10 natural numbers using for loop
for ch in range(1,11):
    print(ch)

num = 1
while num!=11:
    print(num) 
    num+=1

print()
#Python program to print all the even numbers within a given range
for n in range(0,10,2):
    print(n)

num = 0
while num!=12:
    print(num)
    num+=2

print()
#Python program to calculate the sum of all numbers from 1 to a given number
sum = 0
for n in range(5):
    sum+=n
print(sum)

a,n=0,0
while n!=7:
    a+=n
    n+=1
print(a)

print()
#WAP to zip four variables and print the elements wrt their index position
L={23,45,56,12,43,23}
T=("abc","123","000","xyy","mno","789")
s1=(20,30,40,50,60,70)
s2=["ma","ba","ad","ge","md","lt"]
j=zip(L,s1,T,s2)
for var in j:
    print(var)
print(list(zip(L,s1,T,s2)))


k=dict(s2)

for value in k.values():
    print(value)
    print(type(value))
print(type(k.values()))

print()
#WAP to print the factorial
n,fact=5,1
for num in range(1,n+1):
    fact*=num
print(fact)

print()
#WAP to add the elements of a list in the form of list
nums=[2,22,2,2,3]
l=[]
for i in nums:
    l.append([i])
print(l)

print()
#WAP to calculate the sum of all the odd numbers within the given range
letter = 0
for l in range(1,11):
    letter +=l