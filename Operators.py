#Arithmetic Operators
# -Addition Operators
a1 = 4 + 5
print(a1)
a2 = 9.5 + 90.5
print(a2)
a3 = 23 + 45.4
print(a3)
a4 = True + False
print(a4)
a5 = (6+4j)+2j
print(a5)
a6 = (8+2j) + 3.45
print(a6)
a7 = 'butter' + 'fly'
print(a7)
a8 = [2,3,4] + ['5','6']
print(a8)
a9 = ('s','a','d') + (3,)
print(a9,"\n")

# -Subtraction operator
s1 = 2334-(-78)
print(s1)
s2 = -453.8 - 68.879
print(s2)
s3 = (45+10j)-(78+15j)
print(s3)
s4 = {'i','r','o','n','m','a','n'}-{'i','r','o','n'}
print(s4)
s5 = {'i','r','o','n','m','a','n'}-{'b','a','t','m','a','n'}
print(s5,'\n')
s6 = False - True
print(s6)

# -Multiplication Operator
m1 = 98*90
print(m1)
m2 = 98.5 * 00
print(m2)
m3 = (9.4+3j)*(2.3j)
print(m3)
m4 = 'Ha'*3
print(m4)
m5 = ['Get','Set','Go']*3
print(m5)
m6 = ['Get','Set','Go']*0
print(m6)
m7 = ('red','yellow','green')*2
print(m7)
m8 = True * False
print(m8,"\n")

# -True Division Operator
t1 = 89 / 4.3
print(t1)
t2 = 679.345/5.55
print(t2)
t3 = False/True
print(t3)
t4 = (54+7j) / 2
print(t4)
t5 = (54+7j) / (2j)
print(t5,'\n')

# -Floor Division Operator
f1 = 988//78.3
print(f1)
f2 = 78.44//8
print(f2)
f3 = 456.6//5.5
print(f3)
f4 = 456.6//True
print(f4,"\n")

# -Modular Division Operator
d1 = 87.4 % 4.5
print(d1)
d2 = 678 % 6.5
print(d2)
d3 = 45 % True
print(d3)
d4 = False % True
print(d4,"\n")

# -Exponent Operator
e1 = 45 ** 3
print(e1)
e2 = 45.67 ** 0.5
print(e2)
e3= True ** 0.9
print(e3)
e4 = True ** False
print(e4)
e5 = (4j)** 4
print(e5,"\n")

#Comparision operator
l1 = 55>3
print(l1)
l2 = 5<4
print(l2)
l3 = 5==5
print(l3)
l4 = 55!=3
print(l4)
l5 = 4.1>4
print(l5)
l6= 5>=5
print(l6)
l7 = 5<=5
print(l7)
l8= 5.5==5.50
print(l8)
l9 = False<=True
print(l9)
l10 = False==True
print(l10)
l11 = False>=True
print(l11)
l12 = False>True
print(l12)
l13= (5+8j)==(5+8j)
print(l13)
l14 = (5+8j)!=(5+8j)
print(l14,'\n')

#Logical Operator
l1 = 55>3 and 4>2
print(l1)
l2 = 5>4 and 6<2
print(l2)
l3 = 5<4 and a<2
print(l3)
l4 = 55>3 or 4>2
print(l4)
l5 = 5>4 or a>4
print(l5)
l6= 5<4 or 7>5
print(l6)
l7 = not True
print(l7)
l8= not 7>3
print(l8)
l9 = not 7<3
print(l9,'\n')


#assignment Operator
a1 = 90
print(a1)
a1 -= 4.3
print(a1)
a1 += True
print(a1)
a1 *=2
print(a1)
a1 //= 5
print(a1)
a1 /= 8
print(a1)
a1 %=0.5
print(a1)
a1 **= 5
print(a1,'\n')


#Membership operator
n='Sun rise from east to west.'
n1 = 'S' in n
print(n1)
n2 = 'Rise' in n
print(n2)
n3 = 'west' not in n
print(n3)
s = [4,2,0,[],'123',[0]]
n4 = '123' not in s
print(n4)
n5 = [] in s
print(n5)
n6 = 6 in (4,5,6,7)
print(n6)
n7 = 6 in {4,5,6,7}
print(n7)
n8 = 'a' in {'a':4,'b':5}
print(n8,'\n')


#Identity operator
x= 252
y= 252
i1 = x is y
print(i1)
x= 257
y= 257
i2 = x is y
print(i2)
x= 2.5
y= 2.5
i3 = x is y
print(i3)
x= 0
y= 0.0
i4 = x is y
print(i4)
x= True + False
y= False + True
i5 = x is y
print(i5)
x= True
y= False
i6 = x is y
print(i6)
x= (2 + 4j)
y= (2 + 4j)
i7 = x is y
print(i7)
x= "252"
y= "252"
i8 = x is y
print(i8)
x= "2527"
y= "2529"
i9 = x is y
print(i9)
x= ''
y= ''
i10 = x is y
print(i10)
x= []
y= []
i11 = x is y
print(i11)
x= ()
y= ()
i12 = x is y
print(i12)
x= {}
y= {}
i13 = x is y
print(i13)
x= set()
y= set()
i14 = x is y
print(i14,'\n')

#Bitwise operator
b=~7
print(b)
b1=~0
print(b1)
b2=~-12
print(b2)
b5 = 55|21
print(b5)
b6 = 20^6
print(b6,"\n")

#shift operator
b3 = 55>>3
print(b3)
b4 = 44<<4
print(b4)