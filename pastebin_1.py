# 1. Объединение двух словарей
# Напишите функцию, которая объединяет два словаря, складывая значения одинаковых ключей.

# Пример:
dict1 = {'a': 10, 'b': 20}
dict2 = {'a': 5, 'c': 15}
def merge_dicts(dict1, dict2):
   for key, value in dict2.items():
      dict1[key] = dict1.get(key, 0) + value
   return dict1

print(merge_dicts(dict1, dict2))  # {'a': 15, 'b': 20, 'c': 15}

# 2. Поиск ключа в глубоко вложенном словаре (рекурсия)
# Напишите рекурсивную функцию, которая ищет значение по заданному ключу в глубоко вложенном словаре
# Пример:
data = {'a': {'b': {'c': 42}}}
def find_key(data, key):
   if key in data:
      return data[key]
   for k, v in data.items():
      if isinstance(v, dict):
         item = find_key(v, key)
         if item is not None:
            return item
   return None
find_key(data, 'c')  # 42

# 3. Подсчет количества всех ключей (рекурсия)
# Напишите функцию, которая считает общее количество ключей во вложенном словаре.

# Пример:

data = {'a': {'b': {'c': 42}}, 'd': 5}
def count_keys(data):
   count = len(data)
   for key, value in data.items():
      if isinstance(value, dict):
         count += count_keys(value)
   return count
count_keys(data)  # 4

# 4. Фильтрация словаря по условию
# Напишите функцию, которая фильтрует словарь, оставляя только те пары, где значения больше заданного числа.

# Пример:
data = {'a': 10, 'b': 5, 'c': 20}
def filter_dict(data, num):
   return {k: v for k, v in data.items() if v >= num}

print(filter_dict(data, 10))  # {'a': 10, 'c': 20}

# 5. Глубокое копирование словаря (рекурсия)
# Реализуйте функцию глубокого копирования словаря, не используя copy.deepcopy().

# Пример:
data = {'a': {'b': {'c': 42}}}
def copy_dict(data):
   if not isinstance(data, dict):
      return data
   return {k: copy_dict(v) for k, v in data.items()}

print(copy_dict(data))  # Новый независимый объект

# 6. Инвертирование словаря (ключи становятся значениями и наоборот)
# Если значения повторяются, объединять их в список.

# Пример:
data = {'a': 1, 'b': 2, 'c': 1}
def invert_dict(data):
   inverted = {}
   for k, v in data.items():
      if v not in inverted:
         inverted[v] = [k]
      else:
         inverted[v].append(k)
   return inverted

print(invert_dict(data))  # {1: ['a', 'c'], 2: ['b']}

# 7. Проверка, является ли словарь симметричным (ключи и значения одинаковые)
# Пример:
data1 = {'a': 'b', 'b': 'a'}
def is_symmetric(data):
   for k, v in data.items():
      if v not in data or data[v] != k:
         return False
   return True

print(is_symmetric(data1))  # True

data2 = {'a': 'b', 'b': 'c'}
print(is_symmetric(data2))  # False

# 8. Преобразование списка пар в словарь
# Напишите функцию, которая принимает список пар (ключ, значение) и превращает его в словарь.

# Пример:
pairs = [('a', 1), ('b', 2)]
def list_to_dict(pairs):
   return dict(pairs)

print(list_to_dict(pairs))  # {'a': 1, 'b': 2}

# 9. Группировка списка значений по ключам (аналог groupby)
# Напишите функцию, которая группирует значения по ключу.

# Пример:
data = [('a', 1), ('b', 2), ('a', 3)]
def group_by_key(data):
   grouped = {}
   for k, v in data:
      if k not in grouped:
         grouped[k] = [v]
      else:
         grouped[k].append(v)
   return grouped

print(group_by_key(data))  # {'a': [1, 3], 'b': [2]}

# 10. Рекурсивное обновление вложенных словарей
# Напишите функцию, которая обновляет значения во вложенном словаре, если ключ уже существует.

# Пример:
dict1 = {'a': {'b': 1}, 'c': 2}
dict2 = {'a': {'b': 3}, 'c': 4, 'd': 5}
def update_nested_dict(d1, d2):
   for k, v in d2.items():
      if isinstance(v, dict) and k in d1:
         update_nested_dict(d1[k], v)
      else:
         d1[k] = v
   return d1

print(update_nested_dict(dict1, dict2))  # {'a': {'b': 3}, 'c': 4, 'd': 5}