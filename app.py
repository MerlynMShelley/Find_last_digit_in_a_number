a = int(input("Enter the base number"))
b = int(input("Enter the exponent number"))

if a==0 and b==0:
    last_digit = 1

if a==0:
    last_digit = 0

if b==0:
    last_digit = 1

if b%4 == 0:
    res = 4

if b%4!= 0:
    res = b%4

num = pow(a, res)

last_digit = num % 10

print(int(last_digit))
