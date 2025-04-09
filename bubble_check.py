def bubble_sort_even_odd(arr):
   for i in range(len(arr)):
      for j in range(len(arr) - 1):
         if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

   return arr
print(bubble_sort_even_odd([3, 2, 4, 1]))