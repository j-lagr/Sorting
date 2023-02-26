#15, 55, 14, 37, 66, 78, 6, 89, 30, 56
array =[15,55,14,37,66,78,6,89,30,56]

def selectionsort(array):
    for i in range (10):
        firstnum = i
        for n in range (i,11):
            if array[n] < array[firstnum]:
                firstnum = n
        var = array[i]
        array[i] = array[firstnum]
        array[firstnum]= var
        print(array)

selectionsort(array)

