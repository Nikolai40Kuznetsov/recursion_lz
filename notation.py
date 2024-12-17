def transfer(n, b):
    if n < b:
         return str(n)
    n, digit = divmod(n, b)
    return transfer(n, b) + str(digit)
number = int(input("Введите число "))
base = int(input("Введите базу системы счисления "))
print(f"Число {number}, записанное в десятичной системе, в системе с основанием {base} записывется как {transfer(number, base)}")