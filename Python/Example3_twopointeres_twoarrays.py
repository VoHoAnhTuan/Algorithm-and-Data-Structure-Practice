def combine(arr1, arr2):
    i = 0
    j = 0

    ans = []

    # "Iterate until one of the pointers reaches the end of its respective array."
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # "If there are remaining elements in arr1, append them to ans."
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # "If there are remaining elements in arr2, append them to ans."
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = [0, 9, 10]
arr4 = [11, 12, 13, 14]

print(combine(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(combine(arr3, arr4))  # Output: [0, 9, 10, 11, 12, 13, 14]
