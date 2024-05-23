
import pandas as pd

coins = [1, 2, 5, 10, 25, 50]
def find_min_coins(sum):

    memo = [float('inf')]*(sum+1)

    memo[0] = 0

    for c in coins:
        for x in range(c, sum+1):
            memo[x] = min(memo[x], memo[x - c] + 1)

    coins_used = {}
    current_sum = sum
    while current_sum > 0:
        for coin in coins:
            if current_sum >= coin and memo[current_sum] == memo[current_sum - coin] + 1:
                if coin in coins_used:
                    coins_used[coin] += 1
                else:
                    coins_used[coin] = 1
                current_sum -= coin
                break

    return coins_used


if __name__ == "__main__":
    res = find_min_coins(132)

    print(res)