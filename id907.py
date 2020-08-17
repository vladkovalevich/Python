howNumbers = int(input())
numbers = input().split(" ")
result = ""
result = 0
for i in range(len(numbers)):
    if(float(numbers[i]) < 2.5):
        result = numbers[i]
        result1 = i
        print(str(result1)+" "+result)
        break
if(result1==0) :   
    print("Not Found")    

    
