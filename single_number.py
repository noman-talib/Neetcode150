nums = [4,1,2, 1,2]
my_nums = []
for value in nums:
    if value in my_nums:
        my_nums.remove(value)
    else:
        my_nums.append(value)
print(my_nums[0])