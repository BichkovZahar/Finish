def palindrom(func):
    if func == func[::-1]:
        print(func)
        print("Рядок є паліндромом")
    else:
        print(func)
        print("Рядок не є паліндромом")
palindrom("fwf")