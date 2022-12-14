numbers=[10,20,30,40,50,60,70]
target=90

for i in range(0,len(numbers)-1):
    sum = numbers[i] + numbers[i+1]
    if(sum == target):
        print(i,i+1)