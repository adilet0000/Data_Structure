# 1. Print Each Step of Insertion Sort
# Function: insertion_sort_steps(arr)
# Description: Implement insertion sort and print the array after each pass.
def insertion_sort_steps(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
      print(arr)
   return arr

# insertion_sort_steps([3, 2, 1])

# Output:
# [2, 3, 1]
# [1, 2, 3]

# 2. Count the Number of Shifts
# Function: insertion_sort_shift_count(arr)
# Description: Implement insertion sort and return the total number of shifts performed.

def insertion_sort_shift_count(arr):
   count = 0
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
         count += 1
      arr[j + 1] = key
   return count

# print(insertion_sort_shift_count([4, 3, 2, 1]))
# Output:
# 6

# 3. Find the Inserted Element at Each Step
# Function: insertion_sort_inserted_steps(arr)
# Description: Print the element being inserted in each step of insertion sort.
# Example:

def insertion_sort_inserted_steps(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
      print(key)

# insertion_sort_inserted_steps([5, 2, 8, 1])

# 2
# 8
# 1

# 4. Sort in Descending Order
# Function: insertion_sort_descending(arr)
# Description: Modify insertion sort to sort the array in descending order.
# Example:

def insertion_sort_descending(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key > arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
   return arr

# print(insertion_sort_descending([4, 1, 3, 2]))

# Output:

# [4, 3, 2, 1]

# 5. Sort Strings by Length
# Function: sort_strings_by_length(arr)
# Description: Implement insertion sort to sort an array of strings based on their length.
# Example:

def sort_strings_by_length(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and len(key) < len(arr[j]):
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
   return arr

# print(sort_strings_by_length(["apple", "kiwi", "banana"]))
# Output:

# ['kiwi', 'apple', 'banana']

# 6. Sort Strings Alphabetically
# Function: insertion_sort_strings(arr)
# Description: Implement insertion sort to sort an array of strings in alphabetical order.
# Example:

def insertion_sort_strings(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
   return arr

# print(insertion_sort_strings(["banana", "apple", "cherry"]))
# Output:

# ['apple', 'banana', 'cherry']

# 7. Sort Only the First K Elements
# Function: insertion_sort_k_elements(arr, k)
# Description: Sort only the first k elements using insertion sort.
# Example:

def insertion_sort_k_elements(arr, k):
   for i in range(1, k):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
   return arr

# print(insertion_sort_k_elements([4, 3, 2, 1, 5, 6], 3))
# Output:
# [2, 3, 4, 1, 5, 6]


# 8. Find the Maximum Element at Each Step
# Function: insertion_sort_max_steps(arr)
# Description: Print the maximum element found in each step of insertion sort.
# Example:

def insertion_sort_max_steps(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key
      print(max(arr[:i + 1]))

# insertion_sort_max_steps([5, 2, 8, 1])
# Output:
# 5
# 5
# 8

# 9. Sort Only the Even Numbers in the Array
# Function: insertion_sort_evens(arr)
# Description: Sort only the even numbers in an array while leaving odd numbers in place.
# Example:

def insertion_sort_evens(arr):
   even = [i for i in arr if i % 2 == 0]
   even.sort()
   j = 0
   for i in range(len(arr)):
      if arr[i] % 2 == 0:
         arr[i] = even[j]
         j += 1
   return arr

print(insertion_sort_evens([5, 2, 8, 3, 6]))
# Output:

# [5, 2, 6, 3, 8]