numbers=[]
for i in range(0,5):
    inputNumber=int(input("Enter a number: "))
    numbers.append(inputNumber)

max=0
for i in numbers:
    if(i> max):
        max=i
print(max)