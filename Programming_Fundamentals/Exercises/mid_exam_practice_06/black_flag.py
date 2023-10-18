def main():
    days = int(input())
    daily_plunder = int(input())
    expected_plunder = int(input())
    plundered = 0
    plundered = plundering(days, daily_plunder, plundered)
    return printing(expected_plunder, plundered)

def plundering(days_for_plundering, daily_plundering, plunder):
    for day in range(1, days_for_plundering + 1):
        plunder += daily_plundering
        if day % 3 == 0:
            plunder += daily_plundering * 0.5
        if day % 5 == 0:
            plunder -= plunder * 0.3
    return plunder

def printing(expected_plunder, plundered):
    if plundered >= expected_plunder:
        return f"Ahoy! {plundered:.2f} plunder gained."
    else:
        percentage = (plundered / expected_plunder) * 100
        return f"Collected only {percentage:.2f}% of the plunder."

print(main())
