numbers = input().split()

a, b, c = map(int, numbers)

is_equilateral = (a == b) and (b == c)

print(is_equilateral)