

def insertionSort(array):
    
    for i in range(1,len(array)):  
        
        isSorted = False
        j = i       
        while(not isSorted and j >= 1):
          
            if(array[j] > array [j-1]):
                isSorted = True            
            else:
            
                temp = array[j]
                array[j] = array [j-1]
                array [j-1] = temp                           
                j -= 1
    return array
                           
array = [1,2,3,4,5,6,7,8,9,10,0]
print(insertionSort(array))







