t = (1,2,3,4,5)
print(t[0])
# tuple cant be changeble or updated or immutable
# t[0]=7
print(t) #it gives type error. t1=() is a empty tuple 
t1=(1)#wrong way to declare a tuple with single element
t1=(1,) #right way

# tuple methods
t1=(1,2,3,4,5,6)
print(t1.count(1))
print(t1.index(5))