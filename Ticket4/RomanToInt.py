rom = input("rom :")
RomanAlf = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
res = 0
for i in range(len(rom)-1):
    if RomanAlf[rom[i]] >= RomanAlf[rom[i+1]]:
        res += RomanAlf[rom[i]]
    else:
        res -= RomanAlf[rom[i]]
res += RomanAlf[rom[-1]]
print(res)
