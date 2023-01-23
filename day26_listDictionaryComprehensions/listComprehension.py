# list comprehension:
new_list = [expression for item in list]

# challenge 1
a = [1, 2, 3, 4]
new_list = [n + 1 for n in a]
#
# It applies to any secuence: list, tuple, string, range:
[i.lower() for i in "GIOVANNI"] # outputs a list

# It can be used together with conditionals:
students_list = ["Dave", "Beth", "Marianne", "Joseph", "Manu"]

# challenge 2
short_names = [name for name in students_list if len(name) <= 4]
# challenge 3
upper_names = [name.upper() for name in students_list if len(name) >= 5]


# ------------------------------------------------

# Dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

students_list = ["Dave", "Beth", "Marianne", "Joseph", "Manu", "Pier", "Nano", "John", "Maria", "Juana"]
from random import randint

students_score = {student:randint(1, 100) for student in students_list}

# look at the use of tuples and method items()
passing_students = {student:score for (student, score) in students_score.items() if score > 80}
