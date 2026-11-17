array = [12, 14, 4, 6, 1, 467, 82, 335, 34, 94, 9]

n = len(array)
# insertion sort
for j in range(1, n):
    k = array[j]
    ind = j - 1
    while ind >= 0 and array[ind] > k:
        array[ind + 1] = array[ind]
        ind = ind - 1
    array[ind + 1] = k

print('Sorted with insertion sorting array: ', array)

print('\n')

array = [12, 140, 140, 4, 6, 1, 467, 82, 335, 34, 94, 9]

# merge sort
def merge_sort(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left_arr = merge_sort(array[:middle])
    right_arr = merge_sort(array[middle:])
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    sorted_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1

    sorted_arr.extend(left_arr[i:])
    sorted_arr.extend(right_arr[j:])

    return sorted_arr

sorted_array = merge_sort(array)

print('Sorted with merge sorting array: ', sorted_array)