import math
a, b, c = map(float, input().split())
angle_a = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
angle_b = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
angle_c = 180 - angle_a - angle_b
print(angle_a, angle_b, angle_c)
