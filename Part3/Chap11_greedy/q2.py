str = input()

result = int(str[0])

for c in str[1:]:
    digit = int(c)
    if digit <= 1 or result <= 1:
        result += digit
    else:
        result *= digit

print(result)
