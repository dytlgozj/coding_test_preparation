a, b = input().split()

result = []

reversed_a = a[::-1]
reversed_b = b[::-1]

if len(a) < len(b):
    a, b = b, a
    reversed_a, reversed_b = reversed_b, reversed_a

i = 0
carry = 0

while i < len(b):
    if i == 0:
        carry = 0
    else:
        carry = (reversed_a[i - 1] + reversed_b[i - 1] + carry) // 10
    result.append((reversed_a[i] + reversed_b[i] + carry) % 10)
    i += 1

result += reversed_a[i:]

for i in result[::-1]:
    print(i)
