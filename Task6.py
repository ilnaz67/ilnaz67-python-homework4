numbers = input().split()

a, b, c = map(int, numbers)

a2 = a * a
b2 = b * b
c2 = c * c

result = (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)

print(result)