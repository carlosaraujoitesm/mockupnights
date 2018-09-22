

def selectionSort(array):
    
    
    for i in range (len(array)):
        min_index = i
        
        for j in range (i+1,len(array)):       
            if(array[j] < array[min_index]):
                min_index = j 
                
        temp = array [min_index]
        array [min_index] = array[i]
        array[i] = temp 
        
    return array
    
                           
array = [1,3,2,5,4,90,45,110,13,140]
print(selectionSort(array))




