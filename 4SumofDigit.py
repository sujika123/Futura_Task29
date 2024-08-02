n = int(input("Enter the number : "))
sum = 0

while(n>0):
    digit = n % 10
    sum = sum + digit
    n = n//10

print("Sum of digits : ",sum)


# Algorithm

# 1. Read an integer input number.
# 2. initialize the variables  sum = 0
# 3. Repeat Steps 5 to 7 Until n > 0.
# 4. digit = (n % 10) %10 return the last digit of the current number
# 5. sum = sum + digit
#    The variable digit is multiplied three times because we check for a three-digit Armstrong number.
# 6. n = n // 10
#    After processing the last digit, we need to remove it. /10 will give an integer such that the order of the number will be reduced and the next digit will become the last digit.
# 7. Print sum
