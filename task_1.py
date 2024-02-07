import time

# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result

# Динамічне програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    result = {}
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and dp[amount] == dp[amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break
                
    return result

# Тестування
test_sum = 9876

# Жадібний алгоритм
start_time_greedy = time.time()
greedy_result = find_coins_greedy(test_sum)
end_time_greedy = time.time()
greedy_time = end_time_greedy - start_time_greedy

# Динамічне програмування
start_time_dp = time.time()
dp_result = find_min_coins(test_sum)
end_time_dp = time.time()
dp_time = end_time_dp - start_time_dp

print("Жадібний алгоритм результат:", greedy_result)
print("Жадібний алгоритм час:", greedy_time)
print("\nДинамічне програмування результат:", dp_result)
print("Динамічне програмування час:", dp_time)