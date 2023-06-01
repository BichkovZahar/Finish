def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Вихідний список цілих чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Виклик функції для фільтрації парних чисел
even_numbers = filter_even_numbers(numbers)

# Виведення нового списку, що містить парні числа
print(even_numbers)
