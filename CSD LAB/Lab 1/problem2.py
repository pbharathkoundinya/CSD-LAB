a=[]
b=[]
s=input("enter the string:")
for i in s:
    if i.isupper():
        a.append(i)
        
    elif i.islower():
        b.append(i)
    else:
        pass
print("upper case char are :",len(a))
print("lower case char are :",len(b))