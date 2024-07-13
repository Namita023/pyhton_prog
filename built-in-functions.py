#---String---
#split
var ="A perfect practice makes a human perfect"
print(var.split())
print(var.split('e'))
print(var.split('c',2))

#replace
print(var.replace(' ','_'))
print(var.replace(' ','_',3))
print("\n")

#index
print(var.index("a"))
print(var.index("f",var.index('f')+1))
print(var.index('c',12,20))
print("\n")

#find
print(var.find("a",var.find("a",var.find("a",var.find('a')+1)+1)+1))
print(var.find("t"))
print(var.find("m",25,35))
print("\n")

#rindex
print(var.rindex("a",0,var.rindex('a',0,var.rindex("a",0,var.rindex("a")))))
print(var.rindex("r"))
print(var.rindex("r",5,25))
print("\n")

#rfind
print(var.rfind("a"))
print(var.rfind("r",5,25))
print("\n")

#format
r = "perfect"
print("A {} practice makes a human {}.".format(r,r))
print("A {r} {x} makes a {y} {r}.".format(r = "perfect",x="practice",y="human"))
print("A {0} {1} makes a {2} {0}.".format("perfect","practice","human"))

#strip
print(var.strip("A"))
print(var.lstrip("A perfect"))
print(var.rstrip("perfect"))
print(var.strip())

#count
print(var.count("e"))
print(var.count("a"))

#startwith endswith
print(var.startswith("A p"))
print(var.startswith("perfect"))
print(var.endswith("A p"))
print(var.endswith("perfect"))


#---list---
#append
L = [34,45,67,'adv','edt']
L.append("23")
print(L)
L.append(45)
print(L)

#insert
L.insert(3,78)
print(L)
L.insert(0,"abc")
L.insert(-1,"love")
L.insert(-10,"deb")
print(L)

#extend
L.extend([10,78])
L.extend({"hit",34})
L.extend("ab")
L.extend({"f":30,"t":40,True:60})
print(L)

#remove
L.remove(45)
L.remove("t")
print(L)

#pop clear
print(L.pop())
print(L.pop(1))
print(L.pop(8))
print(L)
print(L.pop(-3))
print(L)
L.clear()
print(L)

#join
L1=["Mujhe","toh","pata","hi","hai"]
print("-".join(L1))
print("OOO".join(L1))
print(L1)

#min
L2=[76,78,45,23,90,-23]
print(min(L2))

#max
print(max(L2))

#sort
L2.sort()
print(L2)
L2.sort(reverse=True)
print(L2)
L2.sort(reverse=False)
print(L2)

#reverse
L2.reverse()
print(L2)

#---tuple---
#sorted
T=[76,78,45,23,90,-23]
print(sorted(T))
print(sorted(T,reverse=True))

#index
print(T.index(23))

#count
print(T.count(23))
print(T.count(21))

#---set---
#add
S=set()
S.add(True)
S.add("123")
S.add(123)
print(S)

#update
S.update("ab")
S.update({'x':4,'y':3})
print(S)

#remove
S.remove("a")
print(S)

#discard
S.discard(1)
S.discard(100)
print(S)

#pop
print(S.pop())
print(S.pop())

#intersection
S1={'x',123,'z'}
print(S.intersection(S1))

#union
print(S.union(S1))

#different
print(S-S1)
print(S.difference(S1))

#issubset
print(S.issubset(S1))

#clear
S.clear()
print(S)

#---dictionary---
#update
D={}
D.update({'a':23})
D.update(['b2'])
D.update(('xy',(1,2)))
D.update({'op','nm'})
print(D)

#get
print(D.get("a"))
print(D.get("z"))
print(D.get("z",123))

#setdefault
print(D.setdefault("a"))
print(D.setdefault("z",123))
print(D)

#keys
print(D.keys())

#items
print(D.items())

#pop
print(D.pop("n"))
print(D)

#popitem
print(D.popitem())
print(D.popitem())
print(D)

#fromkeys
print({}.fromkeys(['a','b','c'],"abc"))
print({}.fromkeys(['a','b','c']))

#zip
print(tuple(zip("abc","ran")))
print(tuple(zip("abc","rani")))
print(list(zip("abcd","ran")))