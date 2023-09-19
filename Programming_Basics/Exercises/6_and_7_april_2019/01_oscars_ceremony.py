rent = int(input())

statuette = rent - (rent * 0.3)
food = statuette - (statuette * 0.15)
sound = food / 2

total = rent + statuette + food + sound

print(f"{total:.2f}")