numbers = input().split()

a, b, c = map(int, numbers)

result = (a + b > c) and (a + c > b) and (b + c > a)

print(result)