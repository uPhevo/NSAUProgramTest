'''
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[2,-1,1,-2],[2,0,0,-2],[-1,0,0,1]]
'''
#FourSum
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
'''

#int to roman
RomanAlf = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
num = int(input("num: "))
res = ""
k = 12
while num != 0:
    if list (RomanAlf.keys())[k] <= num:
        res += RomanAlf[list(RomanAlf.keys())[k]]
        num -= list(RomanAlf.keys())[k]
    else:
        k -= 1
print(res)
