str = input()

consecutives = [0, 0]

state = int(str[0])
consecutives[state] += 1

for c in str[1:]:
    digit = int(c)
    if state == digit:
        continue
    else:
        consecutives[digit] += 1
        state = digit

print(min(consecutives))
