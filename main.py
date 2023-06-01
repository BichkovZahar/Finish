a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
count = 0
for i in range(a , b):
    count += i
print(count)