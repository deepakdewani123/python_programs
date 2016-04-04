
##test = input()
##boy,girl = map(int,input("").split())
##print(boy,girl)
##no_of_boys = [int(boy) for boy in input().split()]
##print(no_of_boys)
##no_of_girls = [int(girl) for girl in input().split()]
##print(no_of_girls)
test = 0
while(test != -1):
    n = input("enter a string: ")
    print("string is a palindrome") if n == n[::-1] else print("string is not a palindrome")
    test = int(input())
