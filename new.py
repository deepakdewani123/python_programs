##test = int(raw_input())
##var = 0
##while(var < test):
##    var+=1
##    a,b = map(int,raw_input().split())
##    print(int(a + b))

##test = int(input())
##var = 0
##while(var < test):
##    var+=1
##    a = int(input())
##    for ran in range(1,a+1):
##        if ran % 3 == 0:
##            print("fizz")
##        elif ran % 5 == 0:
##            print("buzz")
##        elif (ran % 3 ==0) and (ran % 5 == 0):
##            print("fizzbuzz")
##        else:
##            print(ran)



##test = int(input())
##nums = [int(test) for test in input("Enter space separated inputs: ").split()]
##for num in nums:
##    for ran in range(1,num+1):
##        if (ran % 3 == 0) and (ran % 5 == 0):
##            print("fizzbuzz")
##        elif ran % 3 == 0:
##            print("fizz")
##        elif ran % 5 == 0:
##            print("buzz")
##        else:
##            print(ran)




##test = input()
##boy,girl = map(int,input().split())
##print(boy,girl)
##no_of_boys = [int(boy) for boy in input().split()]
##print(no_of_boys)
##no_of_girls = [int(girl) for girl in input().split()]
##print(no_of_girls)

##for i in range(1,11):
##    for j in range(1,i):
##        print("*")
##    print("\n")

##import re
##match = re.search(r'[\w\d]+@[\w.]+', 'kumard8308887772@gmail.com')
##if match:
##    print (match.group())  ## 'alice-b@google.com'


import re
match = re.search(r'\d\d\d\d\d\d\d\d\d\d', '83088877722')
if match:
    print (match.group())  ## 'alice-b@google.com'
##str = 'an example word:cat!!'
##match = re.search(r'word:\w+!+', str)
### If-statement after search() tests if it succeeded
##if match:                      
##    print ('found', match.group()) ## 'found word:cat'
##else:
##    print ('did not find')
