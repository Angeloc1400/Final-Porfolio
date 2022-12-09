#Angel Ocampo
#November 1, 2022
#Program lets user pick a number and program determines if its divisabble by 5 and 3, 3, or 5
#then it will print a message ragarding on which one is true
for i in range(1,51):
   print(i)

number = int(input("give me a number from 1 to 50 : \n"))
if number % 3 ==0 and number % 5 ==0:
    print("your number is divisable by 3 and 5!")
elif   number % 3==0:
    print("divisable by 3")
elif number % 5==0:
    print("divisable by 5")
else:
    print("not divisable by 5 or 3")

