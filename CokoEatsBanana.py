list1 = [3,5,11,85,7,52]
n = len(list1)
index = 0
for i in range(1,n):
    if(list1[i]>list1[index]):
        index=i
print(index)