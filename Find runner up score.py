if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    maxm=arr[0]
    count=0
    for i in range(1,n):
        if maxm<arr[i]:
            maxm=arr[i]
    for i in range(n):
        if arr[i]==maxm:
            count=count+1
    print(arr[n-(count+1)])
