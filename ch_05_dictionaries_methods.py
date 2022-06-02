myDict={"fast":"In a fast manner",
"Pankaj":"A coder",
"marks":[1,2,3],
"anotherdict":{"pankaj" : "Kumar"}} 

# first method
print(myDict.keys())
print(list(myDict.keys())) #in a list manner

# second method
print(myDict.values())
print(list(myDict.values())) 

# third method
print(myDict.items()) #it returns the tuple format both key and value
print(list(myDict.items())) 

# 4th method
updateDict={
    "tarun":"friend", #this can be done so many times
    # we have to give both key and value
    # we can also update the existing key value pair
     #for example
    "Pankaj":"A entrepreneur"
}
myDict.update(updateDict) #this syntax updates the dictionary
print(myDict)

# 5th method
print(myDict.get("Pankaj"))
# why can't we use this
print(myDict["Pankaj"]) #but incase if we write like this

# when the not given key is to be searched then 
print(myDict.get("Pankaj2")) 
# the above syntax returns the "none" as Pankaj2 is not present
print(myDict["Pankaj2"])
# this above one returns "KeyError" as Pankaj2 is not present
# so better to use get method

# for more dictionaries methods visit python docs