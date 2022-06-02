# set methods
# 1st method
a=set()
a.add(5)
a.add(6) #adding a value repeatedly doesn't change the set
# a.add([7,4,8]) #typeError unhashable type : List
a.add((7,4,8)) #we can add tuples 
# a.add({7,4,8}) #cannot be done because it is unhashable
print(a)

#2nd method
print(len(a))

# 3rd method
a.remove(5) #removes the element from the set
# a.remove(15) #returns an error because 15 is not present in the set
print(a)

# 4th method
print(a.pop()) #pops out any random value from the set

# 5th methods
print(a.clear()) #clears all the values in the set and returns "No