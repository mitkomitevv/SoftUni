book = input()
book_counter = 0

while True:
    current_book = input()
    if current_book == book:
        print(f'You checked {book_counter} books and found it.')
        break

    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    book_counter += 1
