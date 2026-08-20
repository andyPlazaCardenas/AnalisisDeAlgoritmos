def bubbleSort(arr):
    #print(type(arr))
    #print(len(arr))

    #time.sleep(100)

    n = len(arr)

    for i in range (n):

        for j in range (0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [6,5,3,1,8,7,2,4,5,4,2,6,3,7,9,1,2,5,3,5,9,10,6,5,3,1,8,7,2,4,5,4,2,6,3,7,9,1,2,5,3,5,9,10]

bubbleSort(array)

print("\n")
print("Lista Ordenada: ", array, "\n")
print("-------------------------------")