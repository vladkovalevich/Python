howNumbers = int(input())
numbers = input().split(" ")
result = ""
for i in range(len(numbers)):
    if(int(numbers[i]) < 2.5):
        result = i
        continue
    
