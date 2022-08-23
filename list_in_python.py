list1=[1,2,3,'ram','shyam','hello','world']
list2=[56,65,48,'world','hello']

list1.append('pappu')   # append() method adds element at the end of current list
print(list1)

list2.extend(list1)     # extend() method adds the specified list elements to the end of current list
print(list2)

list1.insert(5,'hi')    # insert(i, x) method adds elemnet to specified index where 'i' is index of element to be placed and x is element
print(list1)

list1.remove('ram')     # remove the first item from the list whose value is equal to 'ram'
print(list1) 

list1.pop(5)           # removes item at the given index and if no index is specified then pop will remove last item from list
print(list1)

list2.clear()           # removes all the elements from list
print(list2)

