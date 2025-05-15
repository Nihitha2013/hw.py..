d1={'Codingal':3,'is':2,'for':2,'Coding':1}
print(str(d1))
x=int(input("Enter the number to check the frequency(3,2,1):"))
r=0
for k in d1:
    if d1[k]==x:
        r=r+1
print("Frequency of",x,":",r)