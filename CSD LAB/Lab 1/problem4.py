l=[]
n=int(input("enter no.of elements :"))
for i in range(n):
    i=int(input("enter element :"))
    l.append(i)
d=max(l)
a=[]
l.remove(max(l))
for i in l:
    a.append(i)
s=2*max(a)

if d>=s:
    print("true")
else:
    print("false")