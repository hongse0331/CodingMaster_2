def gcd(x, y):
    while y is not 0:
        r = x%y
        x = y
        y = r
    return x




for _ in range(int(input())):
    n, *a = map(int, input().split())
    sum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            sum += gcd(a[i], a[j])
    print(sum)

