# 1st question
myDict={
    "Pankha":"fan",
    "dabba":"box",
    "vastu":"thing"
}
print("options are :",myDict.keys())
a=input("Enter the hindi word\n")
# print("The meaning of your word is:",myDict[a]) #this returns the error if the key is not present
print("The meaning of your word is:",myDict.get(a)) #this would return none if the key is not present

# 2nd qustion
# to print unique numbers
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
num6=int(input())
num7=int(input())
num8=int(input())
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

# 3rd question
s={18,"18"} #prints both 18 because both are different one is int and other is string
print(s)

# 4th question
s=set()
s.add(20) #here 20 and 20.0 both are same
s.add(20.0)
s.add("20")
print(s)
print(len(s))