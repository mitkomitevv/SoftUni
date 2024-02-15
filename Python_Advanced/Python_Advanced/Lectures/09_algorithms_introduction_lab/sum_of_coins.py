def sum_coins(coins, target_sum):
    coins.sort(reverse=True)
    coins_used = {key: 0 for key in coins}
    idx = 0
    result = []

    while target_sum > 0 and idx < len(coins):
        coin_to_use = target_sum // coins[idx]
        target_sum = target_sum % coins[idx]

        if coin_to_use:
            coins_used[coins[idx]] = coin_to_use

        idx += 1

    if target_sum != 0:
        print("Error")
    else:
        result.append(f"Number of coins to take: {sum(coins_used.values())}")
        for coin, value in coins_used.items():
            if value > 0:
                result.append(f"{value} coin(s) with value {coin}")

    return "\n".join(result)


available_coins = list(map(int, input().split(', ')))
target = int(input())
print(sum_coins(available_coins, target))

# Really, really slow
# def sum_coins(coins, target_sum):
#     coins.sort(reverse=True)
#     coins_used = {key: 0 for key in coins}
#     coins_count = 0
#     result = []
#
#     while target_sum > 0:
#         for coin in coins:
#             if coin <= target_sum:
#                 coins_used[coin] += 1
#                 target_sum -= coin
#                 coins_count += 1
#                 break
#         else:
#             return 'Error'
#
#     result.append(f"Number of coins to take: {coins_count}")
#     for coin, value in coins_used.items():
#         if value > 0:
#             result.append(f"{value} coin(s) with value {coin}")
#
#     return "\n".join(result)
#
#
# available_coins = list(map(int, input().split(', ')))
# target = int(input())
# print(sum_coins(available_coins, target))
