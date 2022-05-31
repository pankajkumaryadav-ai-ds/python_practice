greeting ="good morning, "
name="pankaj"
print(type(name))
print(greeting + name) #concatination of two strings
c=greeting+name
print(c)

name="pankaj"
print(name[0],name[1],name[2],name[3],name[4],name[5])
print(len(name)) #length of the string
# you cant change the string ,but only you can access

# slicing
print(name[0:3]) #only 0,1,2 but not 3
print(name[1:4])
print(name[:4])#nothing implements first index
print(name[0:])#nothing at last is full and also included the last
# negative slicing or indexing
# when you dont know the length 
# the last one is -1
print(name[-4:-1]) #including 1 upto 3

# skipping the value
a = "pankajisverygoodboy"
print(a[1:4:3])#after second colon skip value
print(a[0::3])#middle left because it should go
# till last and 3 given that it skips 2 in between them