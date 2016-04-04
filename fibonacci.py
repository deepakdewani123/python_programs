n = input("Enter a string to check for palindrome: ")
if(str(n) == str(n)[::-1]):
    print(n+" is a palindrome")
else:
    print(n+" is not a palindrome")

print(n[::-1])
