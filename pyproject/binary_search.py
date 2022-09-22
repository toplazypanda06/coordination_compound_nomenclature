def search(l, s):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end) // 2
        if s == l[mid]:
            return (mid, 1)
        elif s > l[mid]:
            start = mid + 1
        elif s < l[mid]:
            end = mid - 1
    return(mid, -1)
    

l = [1,2,2,4,5,6,7,8,9]
s = 10
index = search(l,s)
if index[0] >= 0 and index[-1] == 1:
    print(index[0], "found")
else:
    print(index[0],"not found")