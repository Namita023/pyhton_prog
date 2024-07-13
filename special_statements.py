for i in range(1,11):
    if i==4:
        break
    print(i)
else:
    print("I'm in else block")

i=1
while i==6:
    if i==4:
        break
    print(i)
    i+=1
else:
    print("I'm in else block")

#breaking inner for loop with inner loop value
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break

print()
#breaking inner for loop with outer loop value
for i in range(1,6):
    for j in range(1,6):
        if i==3:
            break
        print(i,j)


print()
#breaking outer for loop with outer loop value
for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)

print()
#breaking inner for loop with inner loop value
i=1
while i<6:
    j=1
    while j<6:
        if j==4:
            break
        print(i,j)
        j+=1
    i+=1

print()
#breaking inner for loop with outer loop value
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        
        j+=1
    i+=1

print()
#breaking outer for loop with outer loop value
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break
    i+=1

print()
#breaking outer for loop with outer loop value
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==3:
        break
    i+=1