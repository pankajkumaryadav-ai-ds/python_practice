# lists are ordered and changeble
a=[1,2,3,4,5]
a[0]=98
# access using index using a[0],a[1]..etc
print(a)

# we can create a list of different types
c=[45,"Harry",False,6.9]
print(c)

# lists slicing and indexing
friends=["pankaj","kumar","yadav","tarun","sathwik"]
# print(friends)
print(friends[0:4])
print(friends[-4:-2])

# list methods
l1=[1,8,7,2,21,15]
# sorting the list
# l1_sorted=l1.sort()#this will gives none
# print(l1_sorted)
l1.sort()
print(l1)

# reversing the list
l1.reverse()
print(l1)

# appending = adds at the end of the list
l1.append(45)
print(l1)

# inserting
l1.insert(0,544) #first indicates the index position and then the element
print(l1)

# pop
l1.pop(2) #used for removiing the element at that index
print(l1)

# remove
l1.remove(21) #removes the element from the list
print(l1)
# for more python list methods visit python docs only 