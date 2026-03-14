x = 121
if x < 0:
    print("Not a palindrome")

s = str(x)
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")