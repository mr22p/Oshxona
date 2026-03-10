# n = int(input("Ikki xonali son kiriting: "))

# a = n // 10
# b = n % 10

# if a % 2 != 0 and b % 2 != 0:
#     print("Ikkala raqam ham toq")
# else:
#     print("Raqamlardan biri yoki ikkalasi ham toq emas")

# n = int(input("Uch xonali son kiriting: "))

# a = n // 100
# b = (n // 10) % 10
# c = n % 10

# if a == b or a == c or b == c:
#     print("Bir xil raqamlar mavjud")
# else:
#     print("Bir xil raqam yo'q")

# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))

# if a % 2 == 0:
#     print("a juft")
# if b % 2 == 0:
#     print("b juft")
# if a % 2 != 0 and b % 2 != 0:
#     print("Hech biri juft emas")

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a % 2 == 0:
#     print("a juft")
# if b % 2 == 0:
#     print("b juft")
# if c % 2 == 0:
#     print("c juft")

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# count = 0

# if a > 0:
#     count += 1
# if b > 0:
#     count += 1
# if c > 0:
#     count += 1

# print("Musbat sonlar:", count)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# musbat = 0
# manfiy = 0

# if a > 0:
#     musbat += 1
# elif a < 0:
#     manfiy += 1

# if b > 0:
#     musbat += 1
# elif b < 0:
#     manfiy += 1

# if c > 0:
#     musbat += 1
# elif c < 0:
#     manfiy += 1

# print("Musbat:", musbat)
# print("Manfiy:", manfiy)

# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     print(a, b)
# else:
#     print(b, a)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a > 0:
#     print("a kvadrati:", a*a)
# if b > 0:
#     print("b kvadrati:", b*b)
# if c > 0:
#     print("c kvadrati:", c*c)

# import math

# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))

# D = b*b - 4*a*c

# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2*a)
#     print("x1 =", x1)
#     print("x2 =", x2)

# elif D == 0:
#     x = -b / (2*a)
#     print("x =", x)

# else:
#     print("Haqiqiy yechim yo'q")

# n = int(input("1-7 son kiriting: "))

# days = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]

# if 1 <= n <= 7:
#     print(days[n-1])
# else:
#     print("Noto'g'ri son")

# a = int(input("a: "))
# b = int(input("b: "))

# if a > 0 and b > 0 and (a + b) > 100:
#     print("Natija:", a / b)
# else:
#     print("Natija:", a * b)

# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     print(1)
# elif b > a:
#     print(2)
# else:
#     print(0)                    

# for i in range (0,11,2):
#  print(i , end=";")


# for i in range(0,11):
#  print(i , end=";")


# for i in range (10,0,-1):
#  print(i , end=";")

son = int(input("Son kiriting: "))
for son in range(0,son,):
    print(son, end=";")

# son = int(input("Son kiriting: "))
# for son in range(0,son,2):
#     print(son, end=";")
