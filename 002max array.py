arr=[23,53,12,423,6545,12]
n=len(arr)
r=arr[0]
for i in range(1,n):
    r=max(r,arr[i])
print (r)
