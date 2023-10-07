# Abbas Salim
# 2026396
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

x_solution = None
y_solution = None

for x in range(-10, 11):
    for y in range(-10, 11):
        if a*x + b*y == c and d*x + e*y == f:
            x_solution = x
            y_solution = y
            break
    if x_solution is not None:
        break

if x_solution is not None:
    print(x_solution, y_solution)
else:
    print("No solution")
