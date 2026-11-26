def countingSort(arr):
                                                                 
    frequency_array = [0] * 100

                                                            
    for num in arr:
        frequency_array[num] += 1

    return frequency_array


print(countingSort([63, 25, 73, 1, 98]))
