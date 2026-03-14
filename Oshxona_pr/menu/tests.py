# 1. O'zgaruvchilar turini aniqlash

alfa = 579413
beta = 'Aqlbek'
d = True
s = 0
resp = 'd'
b = 100
max_val = False
fc = 'True34'
t = 102.5
res = '2500'
a = '-50'
b = 45.67

print("1-masala: O'zgaruvchilar turlari")
print(type(alfa))
print(type(beta))
print(type(d))
print(type(s))
print(type(resp))
print(type(b))
print(type(max_val))
print(type(fc))
print(type(t))
print(type(res))
print(type(a))


# 2. Qayiqlar uchrashish vaqti
print("\n2-masala: Qayiqlar uchrashish vaqti")

a = float(input("1-qayiq tezligi (km/soat): "))
b = float(input("2-qayiq tezligi (km/soat): "))
S = float(input("Masofa (km): "))

t = S / (a + b)

print("Uchrashish vaqti:", t, "soat")


# 3. Xonaning yuzasi va perimetri
print("\n3-masala: Xona yuzasi va perimetri")

x = float(input("Xona bo'yi: "))
y = float(input("Xona eni: "))

S = x * y
P = 2 * (x + y)

print("Yuza =", S)
print("Perimetr =", P)


# 4. Uchburchak yuzasi
print("\n4-masala: Uchburchak yuzasi")

c = float(input("Asos uzunligi: "))
h = float(input("Balandlik: "))

S = (c * h) / 2

print("Uchburchak yuzasi =", S)


# 5. Avtomobil yurgan vaqt
print("\n5-masala: Avtomobil yurgan vaqt")

v = float(input("Tezlik (km/soat): "))
s = float(input("Masofa (km): "))

t = s / v

print("Yurgan vaqt =", t, "soat")


# 6. Doira yuzasi va aylana uzunligi
print("\n6-masala: Doira yuzasi va aylana uzunligi")

r = float(input("Radius: "))
pi = 3.14

S = pi * r * r
L = 2 * pi * r

print("Doira yuzasi =", S)
print("Aylana uzunligi =", L)