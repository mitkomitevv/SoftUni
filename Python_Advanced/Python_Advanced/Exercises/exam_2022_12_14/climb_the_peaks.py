from collections import  deque

portions = deque(int(x) for x in input().split(', '))
all_stamina = deque(int(x) for x in input().split(', '))

conquered_peaks = []
peaks = [
    ['Vihren', 80],
    ['Kutelo', 90],
    ['Banski Suhodol', 100],
    ['Polezhan', 60],
    ['Kamenitza', 70]
]

while portions and all_stamina and peaks:
    food = portions.pop()
    stamina = all_stamina.popleft()
    result = food + stamina

    if result >= peaks[0][1]:
        conquered_peaks.append(peaks[0][0])
        peaks.pop(0)

print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK" if len(conquered_peaks) == 5
      else "Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:", *conquered_peaks, sep='\n')
