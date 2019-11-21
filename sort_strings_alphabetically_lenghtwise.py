string_list = ['x', 'is', 'alphabet', 'and','you', 'are', 'my','friend']
dummy_list=string_list
# Using sort() function
dummy_list.sort()
print(1,dummy_list)


# Using sorted() function

dummy_list=string_list
print(2,end =" ")
for sorted_values in sorted(dummy_list):
    print(sorted_values,end =" ")


# Using sort() function with key as len
print("\n")
dummy_list=string_list
dummy_list.sort(key=len)
print(3,dummy_list)


# Using sort() function with key as int
int_list = ['23', '33235431', '1145756856846783895789', '7', '5556784578485684577457']
int_list.sort(key=int)
print(4,int_list)



dummy_list=string_list
# alphabetically sort
dummy_list.sort(reverse=True)
print(5,dummy_list)