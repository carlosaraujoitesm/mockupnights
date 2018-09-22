


def countingSort(array):

    max_num = max(array) + 1
    temp = [0] * max_num
    out = [0] * len(array)
    print temp
    #counting
    for i in range(len(array)):
        temp[array[i]] +=1
    #arithmetic to know the last position of each repeated element

    for i in range(1,len(temp),1):  #
        temp[i] = temp[i] + temp[i-1]  
    
    #locate in rigth place
    print temp
    for i in range(len(array)-1,-1,-1):
        if(temp[array[i]] > 0):
            out[temp[array[i]] - 1] = array[i]
            temp[array[i]]-=1
    return out
array = [1,4,1,2,7,5,2]
print(countingSort(array))
