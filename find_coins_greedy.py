coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum):
    coin_set = {}

    while sum > 0:
        for i in range(len(coins)):
            if coins[i] <= sum:
                coin_set[coins[i]] = coin_set[coins[i]] + 1 if coins[i] in coin_set else 1
                sum -= coins[i]
                break

    return coin_set


if __name__ == "__main__":
    print(find_coins_greedy(132))
