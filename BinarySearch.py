#BinarySearch

def BinarySearch(array,val,end,start):
    midval = int((end+start)/2)
    if array[start] == val:
        return print('At ' + str(start) + ' positon')

    elif array[end] == val:
        return print('At the ' +str(end)+ ' index of array')
    
    
    elif array[midval] == val:
        return print('At the ' +str(midval)+ 'index of array')

    else:
        if array[midval] > val:
            restart = start
            end = midval
            array2 = array
            val2 = val
            BinarySearch(array2,val2,end,restart)
        else:
            restart = midval
            end2 = end
            array2 = array
            val2 = val
            BinarySearch(array2,val2,end2,restart)

array = [1,2,3,4,5,6,7,8,9,10]
BinarySearch(array,10,len(array)-1,0)
