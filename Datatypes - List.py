""" What are Lists? Lists are used to store different items in a single Variable. 
For example, your Handbag! You can keep different stuffs in your Handbag. 
Such is Python Lists, Tuples and Dictionaries. 

What makes Lists different? 

The Syntax
The Attribute
To write a List in Python we use the Square Bracket syntax []."""

listname = ["Aptlearn.io", "Udemy", "MyAcademy"]

# no = [1, 2, 3, 4, 5]

# booList = [True, False]

# floatList = [0.0, 0.1, 2.2]

# mixedList = ["String", 1, 0.1, True, 1j]

# repeatList = ["Boy", "Girl", "Boy"] 


# You can use indexing to print items in a list as python uses indexes starting from "0" to print Lists

firstitem = listname[0]
seconditem = listname[1]
thirditem = listname[2]

# you can also use negative index like "-1" to print content of a list,
lastitem = listname[-1]

print(firstitem)
print(seconditem)
print(thirditem)
print(lastitem)

'''You can automatically add an item to your list without 
manually editing the already made list with the 'append' function'''

listname.append("python101")
print(listname)

'''To add a new item in a particular position of your list, 
you use the 'insert' function followed by the index number of the place yu want to place the item''' 

listname.insert(1, "Learn Python")
print(listname)

# To add more than one item at once in a list, use the 'extend' function
listname.extend(["Variables", "Datatypes", "Lists"])
print(listname)

# To remove an item, use the 'remove' function
listname.remove("Udemy")
print(listname)