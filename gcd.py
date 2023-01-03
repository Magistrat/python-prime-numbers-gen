def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return gcd(b % a, a )
    if a > b:
        return gcd(b, a % b)
    if a == b:
        return a

print(gcd(10000, 10000))
