n = int(input())
h = n//3600
m = (n % 3600)//60
s = (n % 3600) % 60
print(h, 'часов', m, 'минут', s, 'секунд')
