import string
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input())
L = []

for i in range(n):
    s = "-".join(a[i:n])
    L.append(s[::-1]+s[1:])

width = len(L[0])

for i in range(n-1, 0, -1):
    print(L[i].center(width, "-"))

for i in range(n):
    print(L[i].center(width, "-"))
