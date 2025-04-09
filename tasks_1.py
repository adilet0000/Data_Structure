# NUMBER 1
# 1r. Sum of Numbers from 1 to N
# Function: sum_n(n)
# Description: Find the sum of numbers from 1 to n.
# Example:
def sum_n(n):
   if n == 0:
      return 0
   return n + sum_n(n - 1)
 
# print(sum_n(5))
# Output:
# 15

# 2r. Reverse a String
# Function: reverse_string(s)
# Description: Reverse a string using recursion.
# Example:
def reverse_string(s):
   return s[::-1]

def reverse_string_recurtion(s):
   return reverse_string_recurtion(s[1:]) + s[0]

# print(reverse_string_recurtion("hello"))
# Output:
# "olleh"

# 3r. Sum of Digits of a Number
# Function: sum_of_digits(n)
# Description: Compute the sum of digits of a number.
def sum_of_digits(n):
   if n == 0:
      return 0
   return n % 10 + sum_of_digits(n // 10)
# Example:
# print(sum_of_digits(123))
# Output:
# 6
 
# 4r. Palindrome Check
# Function: is_palindrome(s)
# Description: Check if a string is a palindrome.
def is_palindrome(s):
   if len(s) <= 1:
      return True
   if s[0] != s[-1]:
      return False
   return is_palindrome(s[1:-1])

# Example:
# print(is_palindrome("racecar"))
# Output:
# True

# 5r. Find Maximum in an Array
# Function: find_max(arr, n)
# Description: Find the maximum element in a list.
def find_max(arr, n):
   for i in range(len(arr)):
      if arr[i] > n:
         return find_max(arr, arr[i])
   return n
# Example:
# print(find_max([1, 5, 3, 9, 2, 12, 44, 11, 24], 5))
# Output:
# 44
 
# 6r. Find a value by key in a nested dictionary 
# find_key(d, key)
# Find the value of a given key in a dictionary that may contain nested dictionaries.  
data = {
    "name": "Alice",
    "info": {
        "age": 25,
        "contact": {
            "email": "alice@example.com",
            "phone": "123-456"
        }
    }
}
def find_key(d, key):
   for k, v in d.items():
      if k == key:
         return v
      if isinstance(v, dict):
         return find_key(v, key)

# print(find_key(data, "email"))
# Output:
# "alice@example.com"
 
# 7r. Find all keys with a specific value 
# find_keys_by_value(d, target_value) 
# Find all keys whose values match `target_value` in a nested dictionary.  
 
data = {
    "name": "Alice",
    "info": {
        "age": 25,
        "details": {
            "name": "Bob",
            "city": "New York",
            "name_2": "Bob"
        }
    }
}

def find_keys_by_value(d, target_value):
   keys = []
   for k, v in d.items():
      if v == target_value:
         keys.append(k)
      if isinstance(v, dict):
         keys.extend(find_keys_by_value(v, target_value))
   return keys

# print(find_keys_by_value(data, "Bob"))
# Output:
# ["name", "name_2"]
 
 
 
 
 
 
# # QuickSort
# 1. Implement QuickSort  
# Function: quick_sort(arr)  
# Implement the basic QuickSort algorithm.  
def quick_sort(arr):
   if len(arr) <= 1:
      return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x > pivot]
   return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort([3, 2, 1]))
# Output:
# [1, 2, 3]
 
# 2. Print Each Step of QuickSort  
# quick_sort_steps(arr)
# Implement QuickSort and print the array at each recursive step.  
# quick_sort_steps([4, 3, 2, 1])
def quick_sort_steps(arr):
   if len(arr) <= 1:
      return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x > pivot]
   print(f"Pivot: {pivot}, Left: {left}, Right: {right}")
   return quick_sort_steps(left) + middle + quick_sort_steps(right)

# Output:
# Pivot: 1, Left: [], Right: [4, 3, 2]
# Pivot: 2, Left: [], Right: [4, 3]
# Pivot: 3, Left: [], Right: [4]
# [1, 2, 3, 4]
 
# 3. Count the Number of Recursive Calls  
# quick_sort_call_count(arr)
# Return the number of recursive calls made during QuickSort.  
def quick_sort_call_count(arr):
   calls = 1
   if len(arr) <= 1:
      return calls
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   right = [x for x in arr if x > pivot]
   return quick_sort_call_count(left) + calls + quick_sort_call_count(right)

print(quick_sort_call_count([4, 3, 2, 1]))
# Output:
# 4

# 4. Find the Pivot Element at Each Step  
# quick_sort_pivots(arr)
# Print the pivot element at each recursive step.  
def quick_sort_pivots(arr):
   if len(arr) <= 1:
      return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x > pivot]
   print(f"Pivot: {pivot}")
   return quick_sort_pivots(left) + middle + quick_sort_pivots(right)

# quick_sort_pivots([5, 2, 8, 1])
# Output:
# Pivot: 5
# Pivot: 2
# Pivot: 1
# Pivot: 8
 
# 5. Sort in Descending Order  
# quick_sort_descending(arr)
# Modify QuickSort to sort the array in descending order. 
# print(quick_sort_descending([4, 1, 3, 2]))
def quick_sort_descending(arr):
   if len(arr) <= 1:
      return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x > pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x < pivot]
   return quick_sort_descending(left) + middle + quick_sort_descending(right)
# Output:
# [4, 3, 2, 1]

# NUMBER 2
# 1. Число в словах
# Напишите рекурсивную функцию, которая принимает число (например, 123) и возвращает его словесное представление ("один два три").
def number_to_words(n):
   units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
   teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
            "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
   tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят",
           "семьдесят", "восемьдесят", "девяносто"]
   hundreds = ["", "сто", "двести", "триста", "четыреста",
               "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
   
   if n == 0:
      return "ноль"
   elif n < 10:
      return units[n]
   elif n < 20:
      return teens[n - 10]
   elif n < 100:
      return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")
   elif n < 1000:
      return hundreds[n // 100] + (" " + number_to_words(n % 100) if n % 100 != 0 else "")
   elif n < 2000:
      return "тысяча" + (" " + number_to_words(n % 1000) if n % 1000 != 0 else "")
   elif n < 5000:
      return units[n // 1000] + " тысячи" + (" " + number_to_words(n % 1000) if n % 1000 != 0 else "")
   else:
      return "слишком большое число"

print(number_to_words(1234))

# 2. Генерация всех возможных скобочных последовательностей
# Дано число n. Нужно сгенерировать все возможные правильные скобочные последовательности длины 2n.

#  n = 3  
# Выход: ["((()))", "(()())", "(())()", "()(())", "()()()"]
 
# 3. Разбиение числа на слагаемые
# Дано число n. Нужно найти все возможные способы разложения его на сумму меньших чисел.
# Пример:
 
# makefile
# Копировать
# Редактировать
# Вход: n = 4  
# Выход:
# [
#   "4",
#   "3 + 1",
#   "2 + 2",
#   "2 + 1 + 1",
#   "1 + 1 + 1 + 1"
# ]
# 4. Обход лабиринта
# Дан двумерный массив maze, где 0 — проходимая клетка, а 1 — стена.
# Задача: Написать рекурсивную функцию, которая находит путь из точки (0,0) в точку (n-1, m-1).
 
# 5. Все перестановки строки
# Напишите рекурсивную функцию, которая находит все возможные перестановки символов строки.
# Пример:
 
# arduino
# Копировать
# Редактировать
# Вход: "abc"  
# Выход: ["abc", "acb", "bac", "bca", "cab", "cba"]
 
# 6. Ханойская башня
# Имеется n дисков, которые находятся на первом стержне. Нужно перенести их на третий стержень, используя второй как вспомогательный, соблюдая правила:
 
# Можно перемещать только по одному диску за раз.
# Нельзя класть больший диск на меньший.
# Вывести последовательность действий.
 
# 7. Генерация всех подмножеств множества
# Напишите рекурсивную функцию, которая генерирует все подмножества множества.
# Пример:
 
# less
# Копировать
# Редактировать
# Вход: [1, 2, 3]  
# Выход: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
 
# 8. Вывод всех возможных маршрутов в сетке
# Дана сетка размером n x m. Робот может двигаться только вправо или вниз. Напишите рекурсивную функцию, которая находит все возможные маршруты из (0,0) в (n-1, m-1).
 
# 9. Код Грея
# Напишите функцию, которая генерирует последовательность кода Грея длины n.
# Пример:
 
# arduino
# Копировать
# Редактировать
# Вход: n = 3  
# Выход: ["000", "001", "011", "010", "110", "111", "101", "100"]
 
# 10. Задача о рюкзаке (Knapsack Problem)
# Дан массив предметов, у каждого есть вес и стоимость. Есть рюкзак с вместимостью W. Напишите рекурсивное решение, которое максимизирует стоимость предметов в рюкзаке.