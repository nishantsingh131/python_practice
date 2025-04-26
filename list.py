list=["Nishant",0,"C"]
print(list)

print(list[1])

list[0]="My"

print(list[0])

#List are Mutable in Nature  you can chnage vlaue but not in string 
'''
In Python, a list is a collection of items that are ordered, changeable (mutable), 
and allow duplicate values.

• l1.sort(): updates the list to [1,2,7,8,15,21]
• l1.reverse(): updates the list to [15,21,2,7,8,1]
• l1.append(8): adds 8 at the end of the list
• l1.insert(3,8): This will add 8 at 3 index
• l1.pop(2): Will delete element at index 2 and return its value.
• l1.remove(21): Will remove 21 from the list. 

'''

list.insert(2,1)
list.append(100)
list.pop(1)
print(list)