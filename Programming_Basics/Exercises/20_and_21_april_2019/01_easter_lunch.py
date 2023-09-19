bread = int(input())
eggs = int(input())
cookies = int(input())

bread_price = bread * 3.20
eggs_price = eggs * 4.35
cookies_price = cookies * 5.40

paint = (eggs * 12) * 0.15

total = bread_price + eggs_price + cookies_price + paint

print(f"{total:.2f}")
