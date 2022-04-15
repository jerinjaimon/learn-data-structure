"""Merge Sort."""


def merge(left, right):
    """Merge."""
    i = 0
    j = 0
    sorted_output = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_output.append(left[i])
            i += 1
        else:
            sorted_output.append(right[j])
            j += 1

    sorted_output.extend(left[i:])
    sorted_output.extend(right[j:])

    return sorted_output


def merge_sort(nums: list) -> list:
    """Divide."""
    length = len(nums)
    if length < 2:
        return nums

    mid = length // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
print(unsorted_list)
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
