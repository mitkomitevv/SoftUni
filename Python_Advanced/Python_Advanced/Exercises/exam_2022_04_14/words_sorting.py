def words_sorting(*words):
    words_dict = {word: sum(ord(char) for char in word) for word in words}

    result = []
    for word, amount in sorted(words_dict.items(), key=lambda x: -x[1] if sum(value for value in words_dict.values()) % 2 != 0 else x[0]):
        result.append(f"{word} - {amount}")

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
