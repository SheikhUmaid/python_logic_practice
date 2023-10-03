def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found the target, return its index
    return -1  # Target not found in the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} is found at index {result}")
else:
    print(f"Element {target} is not in the array")
