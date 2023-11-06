# Abbas Salim
# 2026396
numbers = input().split()

non_negative_numbers = []

for number in numbers:
    num = int(number)
    if num >= 0:
        non_negative_numbers.append(num)

non_negative_numbers.sort()

for num in non_negative_numbers:
    print(num, end=' ')

