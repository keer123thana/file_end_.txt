import os
c1=os.getcwd()
print(c1)

list1=os.walk(c1)
list2=(next(list1))
list3=(list2[2])
print(list3)
for i,txt in enumerate(list3):
    if txt.endswith(".txt"):
        print(i,txt,"is present")
    




