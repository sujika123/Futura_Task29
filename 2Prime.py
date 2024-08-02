n = int(input("Enter the number : "))

if (n>1):
    for i in range(2,n,1):
        if(n%i == 0):
            print(n ,"is not prime number")
            break
    else:
        print(n ,"is prime number")
else:
    print(n ,"is not prime number")



# Algorithm


# 1.     Start
# 2.     Input: n
# 3.     If n > 1: then
#         For i in range 2 to n-1:
#             If n % i == 0: then
#                 Print n is not a prime number
#                 Break
#         Else:
#             Print n is a prime number
# 4.    Else:
#         Print n is not a prime number
# 5.    End
