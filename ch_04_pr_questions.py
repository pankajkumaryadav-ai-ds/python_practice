# first question
# stores fruits names in the list form from the user
f1 = input("Enter Fruit number 1:")
f2 = input("Enter Fruit number 2:")
f3= input("Enter Fruit number 3:")
f4 = input("Enter Fruit number 4:")
f5 = input("Enter Fruit number 5:")
f6 = input("Enter Fruit number 6:")
f7 = input("Enter Fruit number 7:")
myfruitslist =[f1,f2,f3,f4,f5,f6,f7]
print(myfruitslist)

# second question marks in sorted order
f1 = int(input("Enter marks 1:"))
f2 = int(input("Enter marks 2:"))
f3= int(input("Enter marks 3:"))
f4 = int(input("Enter marks 4:"))
f5 = int(input("Enter marks 5:"))
f6 = int(input("Enter marks 6:"))
mymarks=[f1,f2,f3,f4,f5,f6]
mymarks.sort()
print(mymarks)

# 3rd question is checking that tuple doesnt support changable objects

#4th question
# sum a list with 4 numbers
a=[2,4,56,7]
print(a[0]+a[1]+a[2]+a[3]) #when you know the number of numbers 
print(sum(a)) #for all

# 5th question
# count the number of zeros
a=(7,0,8,0,0,9)
print(a.count(0))