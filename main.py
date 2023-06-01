def ex_8(lst):
    rezult = [s for s in lst if s[0].upper()]
    return rezult
user = []
lst = input("Введіть рядок: ")
user.append(lst)
print(ex_8(user))

