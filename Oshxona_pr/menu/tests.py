for i in range(1, 11):
    print(i)

n = int(input("N sonini kiriting: "))
yigindi = 0

for i in range(1, n + 1):
    yigindi += i

print("Yig'indi:", yigindi)

n = int(input("Son kiriting: "))
faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print("Faktorial:", faktorial)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

son = int(input("Son kiriting (0 chiqish uchun): "))

while son != 0:
    son = int(input("Son kiriting (0 chiqish uchun): "))

print("Dastur tugadi")        