#def rangoli(size):
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#    b = (size - 1)
#    print(b)
#    print(a)
#    for i in range(size):
#        print(str(a[(b - i)]))
#size = int(input())
#rangoli(size)

n = int(input())
L = []

for i in range(n):
	s = '-'.join(a[i:n])
	L.append(s[::-1]+s[1:])
print(L)

width = len(L[0])

for i in range(n-1, 0, -1):
    print(L[i].center(width, "-"))
    print(i)
    print(L)
    print(width)

