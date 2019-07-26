import re
n_try = int(input())
n1 = []
for i in range(n_try):
    n = input()
    n1.append(n)
for i in n1:
     if re.search("^[7-9]\d{9}$",i):
      print('YES')
     else:
      print('NO')
