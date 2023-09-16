# Abbas Salim
# 2026396

print(f'Birthday Calculator')
print(f'Current day')
# user inputs
current_month = int(input('Month: \n'))
current_day = int(input('Day: \n'))
current_year = int(input('Year: \n'))
# birthday user inputs
print(f'Birthday')
birth_month = int(input('Month: \n'))
birth_day = int(input('Day: \n'))
birth_year = int(input('Year \n'))
# calculations
diff_year = current_year - birth_year - 1
diff_day = current_day - birth_day
diff_month = current_month - birth_month
if diff_day >= 0 and diff_month >= 0:
    diff_year = diff_year + 1
elif diff_month > 0:
    diff_year = diff_year + 1
else:
    diff_year = diff_year + 0
print(f'You are {diff_year} years old.')
if diff_day == 0 and diff_month == 0:
    print(f'Happy Birthday!')
