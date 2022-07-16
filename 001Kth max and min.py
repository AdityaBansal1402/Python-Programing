arr=[1,12,2321,1,32,12]
arr.sort()
n=len(arr)
r=arr[0]
x=int(input())
print("Kth maximum number: ",arr[n-x])
print("Kth minimum number: ",arr[x-1])


