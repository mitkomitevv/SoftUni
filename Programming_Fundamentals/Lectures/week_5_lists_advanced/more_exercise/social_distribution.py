def wealth_redistribution(money, min_money):
    total_wealth = sum(money)
    if total_wealth < min_money * len(money):
        return "No equal distribution possible"

    while min(money) < min_money:
        poorest = min(money)
        wealthiest = max(money)
        idx_poorest = money.index(poorest)
        idx_wealthiest = money.index(wealthiest)
        money.remove(wealthiest)
        wealthiest = wealthiest - (min_money -poorest)
        money.insert(idx_wealthiest, wealthiest)
        money.remove(poorest)
        poorest = min_money
        money.insert(idx_poorest, poorest)
    return money


initial_money = [int(x) for (x) in input().split(', ')]
minimal = int(input())
print(wealth_redistribution(initial_money, minimal))
