def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]
print(is_palindrome("топот"))
print(is_palindrome("Топот"))
print(is_palindrome("python"))
print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("aboba"))
print(is_palindrome("hello"))