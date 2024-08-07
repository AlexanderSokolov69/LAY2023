def min_operations_to_n(n):
    # Создаем массив для хранения минимального количества операций для каждого числа от 1 до N
    dp = [-1] + [1000] * n

    # Заполняем массив значениями
    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]


# Пример использования функции
n = 32718
print(f"Наименьшее число операций для получения числа {n} из числа 1: {min_operations_to_n(n)}")