# Basic
for i in range(1,151):
    print(i)
#Multiples of Five
for b in range(0,1001,5):
    print(b)
#Counting the Dojo Way
for x in range(101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')   
    else:
        print(x)
    #Whoa, that sucker's huge
num1,num2 = 0, 500000
sum = 0
for s in range(num1,num2+1):
    sum+=s
print(sum)

for w in range(2018, 0, -4):
    print(w)

lowNum, highNum, mult = 5, 30, 3
for r in range(lowNum,highNum):
    if r % mult == 0:
        print(r)