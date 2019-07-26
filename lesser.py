def lesser(a,b):
  if (a % 2 == 0) and (b % 2 == 0):
    print(min(a,b))
  else:
    print(max(a,b))
a= int(input())
b= int(input())

lesser(a,b)
