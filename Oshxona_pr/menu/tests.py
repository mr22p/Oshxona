import math

# 1-masala
a = int(input("Anvar tergan olma: "))
b = int(input("Dilshod tergan olma: "))
c = int(input("Mahmud tergan olma: "))

jami = a + b + c
har_bola = jami // 3
ortib = jami % 3

print("Har bir bola oladi:", har_bola)
print("Ortiqcha olma:", ortib)


# 2-masala
n = int(input("Uzum miqdori (kg): "))

tonna = n // 1000
sentner = n // 100

print("Tonna:", tonna)
print("Sentner:", sentner)
print("Kilogramm:", n)

yashik = n // 25
print("Kerakli yashiklar soni:", yashik)


# 3-masala
hosil = int(input("Hosil miqdorini kiriting (kg): "))

yashik2 = hosil // 25

print("Yashiklar soni:", yashik2)


# 4-masala
matn = "5746+4186+8426+8266"

sonlar = matn.split("+")

yigindi = 0
for i in sonlar:
    yigindi += int(i)

print("Natija:", yigindi)


# 5-masala
F = float(input("F ni kiriting: "))
a = float(input("a ni kiriting: "))

m = F / a

print("Massasi:", m)


# 5-masala berilgan qiymatlar
variantlar = [(25,45),(12,30),(72,90),(150,15)]

for F,a in variantlar:
    m = F / a
    print("F =",F,"a =",a,"m =",m)


# 6-masala
a = 14
b = 8
c = 452
r = 41

S = a + b + a*c
P = math.pi * r**2 + a*c

print("S =", S)
print("P =", P)