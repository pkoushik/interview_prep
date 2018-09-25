def merge(arr, l, m, r):
    none = m - l  + 1
    ntwo = r - m
    i = 0
    j = 0
    L = [0] * none
    R = [0] * ntwo
    for i in range(0, none):
        L[i] = arr[l + i]
        i = i + 1
    for i in range(0, ntwo):
        R[j] = arr[m + 1 + j]
        j = j + 1
    i = 0
    j = 0
    k = l
    while i < none and j < ntwo:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1
    while i < none:
        arr[k] = L[i]
        i = i + 1
        k = k + 1
    while j < ntwo:
        arr[k] = R[j]
        j = j + 1
        k = k + 1

def mergesort(arr, l,r):
    if l < r:
        m = (l + (r - 1)) / 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)

# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7]
print ("Given array is")
for i in arr:
    print(i)
print("Sorted array is")
mergesort(arr,0,len(arr)-1)
for i in arr:
    print(i)
