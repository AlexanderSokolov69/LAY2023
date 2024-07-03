def min_operations_to_n(n):
    # Функция для поиска наименьшего числа операций
    if n == 1:
        return 0

    result = float('inf')

    # Рекурсивный вызов функции для каждой из операций
    if n % 3 == 0:
        result = min(result, 1 + min_operations_to_n(n // 3))
    if n % 2 == 0:
        result = min(result, 1 + min_operations_to_n(n // 2))

    result = min(result, 1 + min_operations_to_n(n - 1))

    return result


# Пример использования функции
n = 32718
print(f"Наименьшее число операций для получения числа {n} из числа 1: {min_operations_to_n(n)}")