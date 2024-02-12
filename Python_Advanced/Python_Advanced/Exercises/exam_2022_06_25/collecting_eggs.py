from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = deque(int(x) for x in input().split(', '))
boxes_filled = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)
    elif egg == 13:
        papers.append(paper)
        papers[0], papers[-1] = papers[-1], papers[0]
    else:
        if paper + egg <= 50:
            boxes_filled += 1
        else:
            continue

print(f"Great! You filled {boxes_filled} boxes." if boxes_filled else "Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
