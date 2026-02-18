nums = [3,4,5,6]
target = int(input("Enter a Target to find the indexes: "))
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] ==target:
            print(i, j)