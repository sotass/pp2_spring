def is_palindrome(word):
    word = word.replace(" ", "").lower() 
    return word == word[::-1]

word = input()
print(is_palindrome(word))