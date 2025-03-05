def mergeSortarr(arr1,arr2):
    arr3=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr3.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr3.append(arr2[j])
        j+=1
    return arr3

arr1=[1,2,3,4,5,6,7,8,9]
arr2=[15,16,17,18,19,20,21,22,23]
arr3 = mergeSortarr(arr1,arr2)
print(arr3)