def reverse(sen):
    words = sen.split()
    words.reverse()
    return ' '.join(words) 

sen = input()
print(reverse(sen))    