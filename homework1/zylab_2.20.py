# Abbas Salim
# 2026396

lemon_j = int(input('Enter amount of lemon juice (in cups):\n'))
water = int(input('Enter amount of water (in cups):\n'))
agave_nec = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n'))
print()
print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{lemon_j:.2f} cup(s) lemon juice')
print(f'{water:.2f} cup(s) water')
print(f'{agave_nec:.2f} cup(s) agave nectar')
print()
user_servings = int(input("How many servings would you like to make?\n\n"))
print(f'Lemonade ingredients - yields {user_servings:.2f} servings')
servings_average = user_servings / servings
new_lemon_j = lemon_j * servings_average
new_water = water * servings_average
new_agave_nec = agave_nec * servings_average
print(f'{new_lemon_j:.2f} cup(s) lemon juice')
print(f'{new_water:.2f} cup(s) water')
print(f'{new_agave_nec:.2f} cup(s) agave nectar\n')
print(f'Lemonade ingredients - yields {user_servings:.2f} servings')
gallon_lemon_j = new_lemon_j / 16
gallon_water = new_water / 16
gallon_agave_nec = new_agave_nec / 16
print(f'{gallon_lemon_j:.2f} gallon(s) lemon juice')
print(f'{gallon_water:.2f} gallon(s) water')
print(f'{gallon_agave_nec:.2f} gallon(s) agave nectar')
