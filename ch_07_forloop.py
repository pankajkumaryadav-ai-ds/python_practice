fruits=["banana","mangoes","watermelon"]
for item in fruits:
    print(item)

# range
for i in range(8): #by default from 0 to 7
    print(i)
# range (start,stop,step_size)
for i in range(1,9,2):
    print(i)

# for loop with else
for i in range(0,9):
    print(i)
else: #this prints when the loop ends after printing upto 8
    print("This is inside else of for")

Break statement is used to break the statement
for i in range(0,9):
    print(i)
    if(i==5):
        break #loop exist
else:
    print("hi") #else part wont run because of unsuccesful termination of for loop statement

# continue statement
for i in range(0,9):
    if(i==5):
        continue #skips the value
    print(i)
else:
    print("Hi") #else part will run

# pass statement
i=4
if(i>0):
    pass #it is a type of null statement instructs to do nothing
while i<6:
    pass
print("Hi pankaj")