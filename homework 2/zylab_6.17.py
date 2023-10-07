# Abbas Salim
# 2026396

user_password = input('')
new_password = ''
for char in user_password:
    if char == 'i':
        user_password = '!'
    elif char == 'a':
        user_password = '@'
    elif char == 'm':
        user_password = 'M'
    elif char == 'B':
        user_password = '8'
    elif char == 'o':
        user_password = '.'
    else:
        user_password = char
    new_password += user_password

new_password = new_password + 'q*s'
print(new_password)
