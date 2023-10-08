def loading_bar(num):
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        current_percent = num // 10
        return f"{num}% [{'%' * current_percent}{'.' * (10 - current_percent)}]\nStill loading..."


percent = int(input())
print(loading_bar(percent))
