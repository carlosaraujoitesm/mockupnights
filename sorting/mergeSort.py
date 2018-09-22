
def merge(array,inicio,mitad,final):
    

    #Temporal arrays
    n1 = (mitad-inicio) + 1
    n2 = (final-mitad)

    L = [0] * n1
    R = [0] * n2

    for i in range(0,n1):
        L[i] = array[inicio +  i]
    
    for i in range (0, n2):
        R[i] = array[mitad + 1 + i]
    
    i = 0
    j = 0
    k = inicio

    while i < n1 and j < n2:
        if L[i] < R[j]:
            array[k] =  L[i]
            i+=1
        else:
            array[k] =  R[j]
            j+=1
        k+=1
    
    while i < n1 :
        array[k] =  L[i]
        i+=1
        k+=1
        
    while j < n2 : 
        array[k] =  R[j]
        j+=1
        k+=1
    return array

        

def mergeSort(array,inicio,final):

    if inicio < final:

        mitad = (inicio + final)/2
        mergeSort(array,inicio, mitad)
        mergeSort(array,mitad+1,final)
        return merge(array,inicio,mitad,final)



array = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(mergeSort(array,0,len(array)-1))