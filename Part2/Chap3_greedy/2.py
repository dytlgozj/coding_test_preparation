n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
max1 = data[0]
max2 = data[1]

max1_cnt = (m // (k + 1)) * k + m % (k + 1)
max2_cnt = m - max1_cnt

count = max1 * max1_cnt + max2 * max2_cnt

print(count)
