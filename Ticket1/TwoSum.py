a = list(map(int,input().split()))
t = int(input())

f = True
for i in range(len(a)):
    if not f:
        break
    for k in range(len(a) - 1):
        if a[i] + a[k] == t:
            print(f"{a[i]} + {a[k]} = {t}")
            f = False
            break
    if f:
        print("Нет пары")
