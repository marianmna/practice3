x, y, n = input().split()
r = int(x)*int(n)
k = int(y)*int(n)
print(r+k//100, 'руб.', k % 100, 'коп.')
