# Function to sort the array
def sort_array(arr):
    return sorted(arr)

# Get input from the user
user_input = input("Enter the array elements separated by spaces: ")

# Convert input string to a list of integers
array = list(map(int, user_input.split()))

# Sort the array
sorted_array = sort_array(array)

# Display the sorted array
print(f"Sorted array: {sorted_array}")
