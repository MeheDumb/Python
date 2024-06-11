"""Loop List"""
print("Loop List:")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])

i = 0;
while i < len(thislist):
    print(thislist[i])
    i = i+1

[print(x) for x in thislist]

'''List Comprehension'''
print('\nList Comprehension:')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x !="apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x <5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x !="banana" else "orange" for x in fruits]
print(newlist)
