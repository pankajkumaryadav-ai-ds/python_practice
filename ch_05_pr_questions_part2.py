# 5th question is to create a empty set
s=set()
print(type(s))

# 6th question
favlang={}
a=input("Enter your favorite language pankaj:")
b=input("Enter your favorite language tarun:")
c=input("Enter your favorite language mahesh:")
d=input("Enter your favorite language ravi:")
favlang["pankaj"]=a
favlang["tarun"]=b
favlang["mahesh"]=c
favlang["rai"]=d
print(favlang)

# 7th question if two names or keys are same i.e.. keys must be unique
favlang={}
a=input("Enter your favorite language pankaj:")
b=input("Enter your favorite language tarun:")
c=input("Enter your favorite language mahesh:")
d=input("Enter your favorite language ravi:")
favlang["pankaj"]=a
favlang["tarun"]=b
favlang["pankaj"]=c #recently value will be added
favlang["ravi"]=d
print(favlang)
s
# 8th question if two values are same i.e.. values may be same

# 9th question
# can you change the values inside a list which is contained in set s
s={8,7,12,"pankaj",[1,2]}
print(s) #unhashable type:list
# hashable means the objects doesnt change and the tuple values cnnot be changed