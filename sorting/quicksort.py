import sys

def get_partitionIndex(arr,left,right):

    i = left
    j = right
    pivot = arr[(left+right)/2]
    while i <= j:

        while arr[i] < pivot:
            i+=1

        while arr[j] > pivot:
            j-=1
        
        if i <= j:
            arr[i],arr[j] =arr[j],arr[i]
            i+=1
            j-=1
   
  
    return i

def quickSort(array,left,right):

    if left >= right:
        print "Already sorted"
        return

    partitionIndex = get_partitionIndex(array,left,right) 

    if left < (partitionIndex-1):
        quickSort(array,left,partitionIndex-1)
    if partitionIndex < right:
        quickSort(array,partitionIndex,right)

    return array

array = [2,9,8,14,6,3,4,20,2,50]
print(quickSort(array,0,len(array)-1))