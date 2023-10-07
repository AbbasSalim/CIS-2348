# Abbas Salim
# 2026396
def is_palindrome(text):
    text = text.replace(" ", "").lower()

    return text == text[::-1]


if __name__ == '__main__':
    input_text = input()

    if is_palindrome(input_text):
        print(input_text, "is a palindrome")
    else:
        print(input_text, "is not a palindrome")
