# Abbas Salim
# 2026396

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width
print(f'Wall area: {area} square feet')
gallons = area / 350
print(f'Paint needed: {gallons:.2f} gallons')
cans = round(gallons)
print(f'Cans needed: {cans} can(s)\n')
color = input('Choose a color to paint the wall:\n')
if color == 'red':
    cost = cans * 35
elif color == 'blue':
    cost = cans * 25
elif color == 'green':
    cost = cans * 23
else:
    print('Wrong color')
print(f'Cost of purchasing {color} paint: ${cost}')
