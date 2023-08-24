#Task1
num1 = int(input("writt a number"))
num2 = int(input("writt a 2 number"))
num3 = int(input("writt a 3 number"))

print(num1)
if num1 %2 == 0:
    print("your 1 number is even")
else:
    print("your 1 number is odd")
if num2 %2 == 0:
    print("your 2 number is even")
else:
    print("your 2 number is odd") 
if num3 %2 == 0:
    print("your 3 number is even")
else:
    print("your 3 number is odd")
print("And the sum of them is ", num1 + num2 + num3 )   


#Task2
num1 = int(input("writt a number"))
num2 = int(input("writt a 2 number"))
num3 = int(input("writt a 3 number"))

print("your 1 number is",num1)
print("your 2 number is",num2)
print("your 3 number is",num3)

print("And the sum of them is ", num1 + num2 + num3 ) 

#Task3
num1 = int(input("writt a number"))
num2 = int(input("writt a 2 number"))
num3 = int(input("writt a 3 number"))
num4 = int(input("writt a 3 number"))
num5 = int(input("writt a 3 number"))

print("your 1 number is",num1)
print("your 2 number is",num2)
print("your 3 number is",num3)
print("your 4 number is",num4)
print("your 5 number is",num5)
print("your max number is ", max(num1,num4,num2,num3,num5))


#Task4
num = int(input("writt a number"))
print("Divisors of", num, "are")
for i in range(1, num +1):
    if num % i == 0:
        print(i)



#Task5
num1 = int(input("writt a number"))
num2 = int(input("writt a 2 number"))
num3 = int(input("writt a 3 number"))

print(num1)
if num1 %3 == 0:
  print("your 1 number is even and is divisible by 3")
elif num1 %2 == 0:
    print("your 1 number is even ") 
else:
    print("your 1 number is odd")
if num2 %3 == 0:
    print("your 2 number is even and is divisible by 3")
elif num2 %2 == 0:
    print("your 2 number is even ")
else:
    print("your 2 number is odd") 
if num3 %3 == 0:
    print("your 3 number is even and is divisible by 3")
elif num3 %2 == 0:
    print("your 3 number is even ")
else:
    print("your 3 number is odd")
 

 #Task6

num = int(input("writt a number"))

if num > 0 and num %2 == 0 and num %7 == 0:
        print(num,"is positive, odd and divisible by 7" )
else:
    print("no luck")
