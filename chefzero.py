n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)
arr = [[0 for i in range(m)] for j in range(n)]
arr2 = [[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    arr1 = [int(i) for i in input().split()]
    arr[i] = arr1
sumr = 0
for i in arr:
    sumr+=sum(i)
ans = sumr//k+1
curr_sum = 0
k_r = 1
#print(ans,sumr)
for i in range(n):
    for j in range(m):
        curr_sum+=arr[i][j]
        arr2[i][j] = k_r
    if curr_sum>=ans:
        curr_sum = 0
        k_r+=1

for i in range(n):
    for j in range(m):
        print(arr2[i][j],end=' ')
    print()
            
