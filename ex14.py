n = int(input())
print(round((n/(360/60))/5), 'часов', round(((n/(360/60)) % 5)*12), 'минут')
