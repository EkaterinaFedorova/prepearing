def remove_zeroes(input_array):
    for i in range(len(input_array) - 1, -1, -1):
        if input_array[i] == 0:
            del input_array[i]


array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
remove_zeroes(array)
print(array)
