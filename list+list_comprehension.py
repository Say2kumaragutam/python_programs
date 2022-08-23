'''
INPUT : "Sky is blue"
OUTPUT : "blue is sky"

step 1: use split() which seperate every word using ',' i.e. comma
step 2: use slicing to print list in reverse order
step 3: use join() that takes all items in an iterable and joins them into one string
'''
str="sky is blue"
list=str.split()   # if nothing is passed to split function it will consider space
mylist=list[::-1]   # slicing if list items/elements
my_list=" ".join(mylist)
print(my_list)

# we can think of one liner code for above problem
str1="My name is khan"
print(" ".join(str1.split()[::-1]))

# Above example best demonstrate list and list_comprehension
# what we have done in list comprehension is as -
# we replaced variable name with value assigned to that particular variable
# repalced 'list' varaible with 'list' value in slicing
# replaced 'mylist' variable with 'mylist' value
# Lastly, enclosed whole expressions with print() to print output
