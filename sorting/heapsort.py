


def heapify(array,n,i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] > array[i]:
        largest = l
    
    if r < n  and  array[r] >  array[largest]:
        largest = r


    if largest != i:
        array[i],array[largest] =   array[largest] , array[i]
        heapify(array,n,largest)


def heapSort(array):

    #length of the array
    n = len(array)

    #build the max heap, check all the indexes from last node of heap to first.
    for i in range(n-1,-1,-1):
        heapify(array,n,i)

    #iterate elements
    for i in range(n-1,0,-1):
         array[i],array[0] =   array[0] , array[i]
         heapify(array,i,0)

    print(array)
array = [ 12, 11, 13, 5, 6, 7]
heapSort(array)
