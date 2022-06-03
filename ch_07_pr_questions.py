# # 1st question
# # multiplication table using for loop
# num=int(input("Enter the number"))
# for i in range(1,11):
#     # print(str(num)+ "X" + str(i) + "=" + str(i*num))
#     # f string
#     print(f"{num} X {i} = {num*i}")

# # 2nd question
# l1=["Pankaj","sohan","sachin","rahul"]
# for name in l1:
#     if name.startswith("s"):
#         print("Hello "+name)

# #4th QUESTION
# num=int(input("Enter the number:"))
# prime=True #we assume the number is prime
# for i in range (2,num):
#     if(num%i==0):
#         prime=False
#         break
# if prime:
#     print("prime number")
# else:
#     print("not prime")

# # 6th question
# # factorial of number
# num=int(input("number is:"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print("factorial is",factorial)

# 7th question
n=3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))



#8th question
# n=4
# for i in range(4):
#     print("*" * (i+1))