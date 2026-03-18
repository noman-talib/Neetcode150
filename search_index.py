nums = [2, 3, 6, 8]
target = int(input("Enter the targeted element: "))

if target < 1:
    print("Enter a valid number")
elif target in nums:
    print(f"Target found at index: {nums.index(target)}")
else:
    nums.append(target)
    nums = sorted(nums)
    print(f"Target not found. Updated list: {nums}")