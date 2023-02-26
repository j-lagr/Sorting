#15, 55, 14, 37, 66, 78, 6, 89, 30, 56
array =[15,55,14,37,66,78,6,89,30,56]
print("Sorting....")
def selectionsort(array):
    for i in range (9):
        firstnum = i
        for n in range (i,10):
            if array[n] < array[firstnum]:
                firstnum = n
        var = array[i]
        array[i] = array[firstnum]
        array[firstnum]= var
        print(array)

selectionsort(array)
final =str(array)
final = final.replace("[","")
final = final.replace("]","")
print()
print("--------------------------------------------------")
print("|                 Selection Sort                 |")
print("|                                                |")
print("|    ",final,"     |")
print("|                                                |")
print("--------------------------------------------------")