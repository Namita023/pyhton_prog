n=5

#A
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=(n-1)) or (j==0 and i!=0) or (j==(n-1) and i!=0) or (i==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('')

print("\n")

#B
for i in range(n):
    for j in range(n):
        if ((j==0) or (i==0 and j<n-1) or (i==n-1 and j<n-1) or (i==n//2 and j<n-1) or (1<=i<=(n+1/2)-2 and j==n-1 and i!=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#C
for i in range(n):
    for j in range(n):
        if (j==0) or (i==0) or (i==(n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#D
for i in range(n):
    for j in range(n):
        if ((j==0) or (i==0 and j<n-1) or (i==n-1 and j<n-1) or (1<=i<=(n+1/2)-2 and j==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#E
for i in range(n):
    for j in range(n):
        if ((j==0) or (i==0) or (i==n-1) or (i==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#F
for i in range(n):
    for j in range(n):
        if ((j==0) or (i==0) or (i==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#G
for i in range(n):
    for j in range(n):
        if (j==0) or (i==0) or (i==(n-1) and j!=(n-1)) or (j==n-1 and (n//2)<=i<=(n-2)) or (i==n//2 and (n//2)<j<n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#H
for i in range(n):
    for j in range(n):
        if ((j==0) or (j==n-1) or (i==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#I
for i in range(n):
    for j in range(n):
        if ((i==0) or (i==n-1) or (j==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#J
for i in range(n):
    for j in range(n):
        if ((i==0) or (0<=j<=n//2 and i==n-1) or (j==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#K
for i in range(n):
    for j in range(n):
        if (j==0) or (i==0 and j!=(n-1)) or (i==(n-1) and j!=(n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#L
for i in range(n):
    for j in range(n):
        if ((j==0) or (i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#M
for i in range(n):
    for j in range(n):
        if ((j==0) or (j==n-1) or (i==j and i<=n//2) or (((i+j)==(n-1)) and i<=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#N
for i in range(n):
    for j in range(n):
        if ((j==0) or (j==n-1) or (i==j)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#O
for i in range(n):
    for j in range(n):
        if ((i==0) or (j==n-1) or (j==0) or (i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#P
for i in range(n):
    for j in range(n):
        if ((i==0) or (i==n//2) or (j==0) or (j==n-1 and i<=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#Q
for i in range(n):
    for j in range(n):
        if ((i==0 and 1<=j<=n//2) or (j==n-2 and 1<=i<=n//2) or (j==0 and 1<=i<=n//2) or (i==n-2 and 1<=j<=n//2) or (i==j and (n-1)>=j>=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#R
for i in range(n):
    for j in range(n):
        if ((i==0) or (i==n//2) or (j==0) or (j==n-1 and i<=n//2) or (i==j and (n-1)>=j>=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#S
for i in range(n):
    for j in range(n):
        if ((i==0) or (i==n//2) or (j==0 and i<=n//2) or (j==n-1 and i>=n//2) or (i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#T
for i in range(n):
    for j in range(n):
        if ((i==0)or (j==n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#U
for i in range(n):
    for j in range(n):
        if ((j==n-1) or (j==0) or (i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#W                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  cv
for i in range(n):
    for j in range(n):
        if ((i==j and (n//2)<=i<=(n-1)) or (j==n-1) or (j==0) or (i+j==n-1 and 0<=j<=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

print("\n")

#X
for i in range(n):
    for j in range(n):
        if ((i==j) or ((i+j)==(n-1))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#Y
for i in range(n):
    for j in range(n):
        if ((i==j and i<=n//2) or ((i+j)==(n-1))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("\n")

#Z
for i in range(n):
    for j in range(n):
        if ((i==0) or ((i+j)==(n-1)) or (i==n-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()