from collections import deque

bullet_price = int(input())
gun_clip_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
pay = int(input())
bullets_used = 0
clip_size = gun_clip_size

while locks and bullets:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)

    clip_size -= 1
    bullets_used += 1
    if clip_size == 0 and bullets:
        clip_size = gun_clip_size
        print('Reloading!')

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${pay - (bullets_used * bullet_price)}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
