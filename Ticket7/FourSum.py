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
