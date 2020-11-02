def quicksort(array = [9,8,7,-6,5.2,6,2,7,-8,4,6,3,7,2,9,5,8,0,-4,3,3,2,1]):
    if len(array) < 2:
        return array

    pivotValue, leftArray, equalArray, rightArray = array[len(array) // 2], [], [], []
    
    for value in array:
        if value < pivotValue:
            leftArray.append(value)
        elif value == pivotValue:
            equalArray.append(value)
        else:
            rightArray.append(value)

    return quicksort(leftArray) + equalArray + quicksort(rightArray)

print(quicksort())