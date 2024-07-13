year= 2500

#if else
if((year%400==0) or (year%4==0 and year%100!=0)):
    print("Leap Year")
else:
    print("Not a leap year")

#nested if else
if(year%100==0):
    if(year%400==0):
        print("Leap Year")
    else:
        print("Not a leap year")
else:
    if(year%4==0):
        print("Leap Year")
    else:
        print("Not a leap year")

#elif 
if(year%400==0):
    print("Leap Year")
elif(year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")

#ternary operator
print("Leap Year" if ((year%400==0) or (year%4==0 and year%100!=0)) else "Not a leap year")