""" Quick Sort."""


def partition(nums, left, right):
    """ Partitioning array/list."""
    i = left - 1
    pivot = nums[right]
    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[right] = nums[right], nums[i+1]
    return i+1


def quick_sort(nums, left, right):
    """ Recursively do quick sort."""
    if left < right:
        # Gets the index of pivot in sorted aaray
        pivot_index = partition(nums, left, right)
        print(nums[pivot_index], nums)
        quick_sort(nums, left, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, right)


# Driver code
array = [10, 7, 8, 9, 1, 5]
print(f'Unsorted array: {array}')
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')
