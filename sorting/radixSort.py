


def countingSort(array,exp,max_num):

  
    count = [0] * 10
    out = [0] * len(array)
    #counting
    for i in range(len(array)):
        index = (array[i]/exp) % 10
        count[index] +=1


    #arithmetic to know the last position of each repeated element
    for i in range(1,len(count),1):  #
        count[i] = count[i] + count[i-1]  
  
    #locate in rigth place
    for i in range(len(array)-1,-1,-1):
        index = (array[i]/exp) % 10
        if(count[index] > 0):
            out[count[index] - 1] = array[i]
            count[index]-=1
    return out
    

def radixSort(array):

    max_num= max(array)
    exp = 1
    while((max_num/exp) > 1):
        array = countingSort(array,exp,max_num)
        exp*=10
    return array
    
array = [ 170, 45, 75, 90, 802, 24, 2, 66]
print array
print(radixSort(array))


