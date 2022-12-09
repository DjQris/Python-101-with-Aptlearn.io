# Tuples stores different items in a variable just like LISTS,
# The difference is that they're IMMUTABLE(cannot be changed any time,
# In otherwords, Tuples are OBJECTs separated by a comma(,). It can carry different data types
# syntax: (Tuple1, Tuple2, Tuple3) 0r ("Strings", int, floats, complex int, boolean)

tuple1 = ("Tuple", 1, 0.2, -2.5, 2j, True)
print(tuple1)

# To confirm the class of variable above, use the "type" function, see below;
print(type(tuple1))

'''Also, note that tuples can also come without the brackets, 
i.e computer can still see them as tuples as long as it's separated with commas'''

tuple2 = "Python", 3, 0.5, -1.7, 2j, False
print(tuple2)

# confirm data type;
print(type(tuple2))

# To count the number of a particular object(s) that appear in variable;
tuple3 = "Amaka", "Chinedu", "Afam", "Ijeoma", "Amaka"
print(tuple3.count("Amaka"))
print(tuple3.count("Afam"))

# Nested tuple: A tuple inside a Tuple;
nested_tuple = ("Numbers", ("One", "Two", "Three"), "Alphas", ("A", "B", "C"))
print(nested_tuple)

# To print an item using 'index' in the tuple, use [] with the index number;
tuple4 = "cake", "tooth", "money", "torch"
print(tuple4[0])

# To print more items after the indexed one, put the index number followed by ':',
tuple4 = "cake", "tooth", "money", "torch"
print(tuple4[0:])