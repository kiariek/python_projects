def replace_word():
    words = 'Make America great again!'
    words_to_replace = input("Enter the word to replace: ")
    words_to_replace_with = input("Enter the word to replace with: ")
    print(words.replace(words_to_replace,words_to_replace_with))

replace_word()