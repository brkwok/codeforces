a,b,n = map(int, input().split())

# time complexity: O(log(min(a,b)))
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

while n > 0:
    n -= gcd(a, n)
    if n <= 0:
        print(0)
        break
    n -= gcd(b, n)
    if n <= 0:
        print(1)
        break
