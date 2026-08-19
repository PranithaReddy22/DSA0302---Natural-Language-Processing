import math


data = 3
data_science = 3
science_is = 2
science_drives = 1
total = 12


p = data_science / data
print("P(science|data) =", p)


print("P(improves) =", 0)


p3 = 2 / 3
p2 = 2 / 3
p1 = 2 / total

p = 0.5 * p3 + 0.3 * p2 + 0.2 * p1
print("Interpolated P(is) =", round(p, 4))


x, y = 0.66, 0.33

H = -(x * math.log2(x) + y * math.log2(y))
print("Entropy =", round(H, 4))