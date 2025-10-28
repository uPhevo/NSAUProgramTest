def to_base(n, b):
    r = ""
    while n:
        r = str(n % b) + r
        n //= b
    return r or "0"

print(to_base(45, 5))  # n = Число на вход, b = система счисления
