# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_array = [0] * elements
    # TO-DO
    # Set all indexes to 0 to start
    l_idx = r_idx = m_idx = 0

    # Checks which of the two starting elements is smaller
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged_array[m_idx] = left[l_idx]
            m_idx += 1
            l_idx += 1
        else:
            merged_array[m_idx] = right[r_idx]
            m_idx += 1
            r_idx += 1

    # Adds any leftover items to the array if one of the arrays had more elements
    while l_idx < len(left):
        merged_array[m_idx] = left[l_idx]
        m_idx += 1
        l_idx += 1

    while r_idx < len(right):
        merged_array[m_idx] = right[r_idx]
        m_idx += 1
        r_idx += 1

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    # Floor division to find the middle and then breaking the array up based on that position
    middle = len(arr) // 2
    # Recursive calls to break everything down into small sets
    left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
