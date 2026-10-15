text = input('Please enter a sentence of your choice: ').split()

count = len(text)

print('Total words:',count)

longest_word = None

for word in text:
    word_length = len(word)

    if longest_word is None:
        longest_word = word

    elif word_length > len(longest_word):
        longest_word = word

print('Longest word:',longest_word)
