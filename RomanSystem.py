'''
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[2,-1,1,-2],[2,0,0,-2],[-1,0,0,1]]
'''
nums = [int(num) for num in input('nums = ').split(' ')]

nums = []
for num in input("nums = ").split(' '):
       nums.append(int(num))

target = int(input("target = "))
res = []
for i in range(len(nums)-3):
       for j in range(i+1, len(nums)-2):
              for k in range(j+1, len(nums)-1):
                     for n in range(k+1,len(nums)):
                            if((nums[i] + nums[j] + nums[k] + nums[n]) == target and
                               sorted([nums[i], nums[j], nums[k], nums[n]]) not in res):
                                   res.append(sorted([nums[i], nums[j], nums[k], nums[n]]))
print(res)

# Сумма двух

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
