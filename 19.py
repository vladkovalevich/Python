rtry = input()
result = 0
for i in range(int(len(rtry) /2)):
        if(rtry[i] == rtry[-i-1]):
                result +=1
if(int(len(rtry) % 2 ) != 0):
    result +=1
print(result)
