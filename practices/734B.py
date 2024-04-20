k2, k3, k5, k6 = map(int, input().split())

res = 0

res += min(k2, k5, k6) * 256
k2 -= min(k2, k5, k6)
res += min(k2, k3) * 32

print(res)