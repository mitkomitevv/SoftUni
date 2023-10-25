def add(shelf, book):
    if book not in shelf:
        shelf.insert(0, book)
    return shelf

def take(shelf, book):
    if book in shelf:
        shelf.remove(book)
    return shelf

def swap(shelf, book1, book2):
    if book1 in shelf and book2 in shelf:
        index1 = shelf.index(book1)
        index2 = shelf.index(book2)
        shelf[index1], shelf[index2] = shelf[index2], shelf[index1]
    return shelf

def insert(shelf, book):
    if book not in shelf:
        shelf.append(book)
    return shelf

def check(shelf, index):
    if 0 <= index < len(shelf):
        print(shelf[index])

def main():
    shelf = input().split('&')
    input_line = input().split(' | ')
    while input_line[0] != 'Done':
        command = input_line[0]
        if command == 'Add Book':
            book = input_line[1]
            shelf = add(shelf, book)
        elif command == 'Take Book':
            book = input_line[1]
            shelf = take(shelf, book)
        elif command == 'Swap Books':
            book1 = input_line[1]
            book2 = input_line[2]
            shelf = swap(shelf, book1, book2)
        elif command == 'Insert Book':
            book = input_line[1]
            shelf = insert(shelf, book)
        elif command == 'Check Book':
            index = int(input_line[1])
            check(shelf, index)
        input_line = input().split(' | ')
    print(*shelf, sep=', ')
if __name__ == '__main__':
    main()