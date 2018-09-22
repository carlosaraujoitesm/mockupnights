


def bubbleSort(array):

    isSorted = False
    lastUnsorted = len(array)-1
    
    while(not isSorted):
    
        isSorted = True 

        for i in range(lastUnsorted): 
            
                if(array[i] > array[i+1]):
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    isSorted = False
                    
        lastUnsorted-=1
    return array


array = [10,8,6,4,2, 1, 2, 3, 4, 5,0]
print(bubbleSort(array))




