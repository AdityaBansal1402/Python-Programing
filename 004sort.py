arr=[0,1,0,2,1,0,2]
n=len(arr)

for i in range (0,n):
    for u in range(i,n):
        if(arr[i]>arr[u]):
            arr[i],arr[u]=arr[u],arr[i]

print (arr)
