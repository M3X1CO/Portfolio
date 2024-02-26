nums = [22, 99, 82, 101, 82, 198]
nums.sort()
print(nums[2], nums[-2])
for item in nums:
    if(item %2 != 0):
        print("***")