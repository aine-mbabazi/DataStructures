my_tuple1 = (100,200,300,400,500)
my_tuple2 = (600,700,800,900,1000)
# tuple length
print(len(my_tuple1))

# tuple concatenation
my_tuple3 = my_tuple1+my_tuple2
print(my_tuple3)

# Checking for an element in a tuple
print(my_tuple1[1])

# tuple repition
print(my_tuple1*2)

# iteration(multiplies each element in the tuple)
for a in my_tuple2 : print(a*2)

print(type(my_tuple3))

print(type(my_tuple2))

# Adding elements 
tuple_list = list(my_tuple2)
tuple_list.append("Data")
print(tuple_list)

tuple_list = tuple(tuple_list)
print(tuple_list)


