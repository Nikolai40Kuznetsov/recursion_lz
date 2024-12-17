def transfer(n, b):
    if n < b:
        if n == 10:
            n = "A"
        if n == 11:
            n = "B"
        if n == 12:
            n = "C"
        if n == 13:
            n = "D"
        if n == 14:
            n = "E"
        if n == 15:
            n = "F"
        return str(n)
    n, digit = divmod(n, b)
    if digit == 10:
         digit = "A"
    if digit == 11:
         digit = "B"
    if digit == 12:
         digit = "C"
    if digit == 13:
         digit = "D"
    if digit == 14:
         digit = "E"
    if digit == 15:
         digit = "F"
    return transfer(n, b) + str(digit)
number = int(input("Введите число "))
base = int(input("Введите базу системы счисления "))
print(f"Число {number}, записанное в десятичной системе, в системе с основанием {base} записывется как {transfer(number, base)}")