import random
n=int(input("Enter The Count For Password Length:"))
p=set()
c=0
final= ""
while c<n:
    r=random.randint(45,126)
    p.add(chr(r))
    c+=1
for i in p:
    final+=i
print(final)