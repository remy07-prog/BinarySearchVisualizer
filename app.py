# Binary Search function with a few helpful comments
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Repeat until the search space is empty
    while low <= high:
        mid = (low + high) // 2  # Middle index
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found

        # If target is smaller, search the left half
        elif mid_value > target:
            high = mid - 1

        # If target is larger, search the right half
        else:
            low = mid + 1

    return -1  # Target not found



# ---- MAIN PROGRAM ----

# Ask the user to enter a list of numbers separated by commas
user_input = input("Enter a list of numbers (comma-separated): ")
arr = list(map(int, user_input.split(",")))  # Convert text into list of integers

# Ask for a target number to search for
target = int(input("Enter the number to search for: "))

# Sort the list (Binary Search only works on sorted lists)
arr.sort()

# Call the binary search function
result = binary_search(arr, target)

# Display the result
if result != -1:
    print(f"Target found at index {result} in the sorted list {arr}")
else:
    print(f"Target not found in the list {arr}")
