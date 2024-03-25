nums = list(map(int, input().split()))
nums.sort()

print(nums[3] - nums[0], nums[3] - nums[1], nums[3] - nums[2])