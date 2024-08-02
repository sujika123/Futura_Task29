n = int(input("Enter the number : "))
temp = n
sum = 0
while(temp > 0):
    digit = temp%10
    sum = sum + digit ** 3
    temp = temp // 10

if(n == sum):
    print(n, "is Amstrong")
else:
    print(n,"is not Amstrong")



# Algorithm

# 1. Read an integer input number.
# 2. initialize the variables  sum = 0 and temp = n
# 3. Repeat Steps 4 to 6 Until temp > 0.
# 4. digit = (temp % 10) %10 return the last digit of the current number
# 5. sum = sum + (digit * digit * digit).
#    The variable digit is multiplied three times because we check for a three-digit Armstrong number.
# 6. temp = temp // 10
#    After processing the last digit, we need to remove it. /10 will give an integer such that the order of the number will be reduced and the next digit will become the last digit.

# 7. Check if n == sum. Then Print “It is an Armstrong Number.”
# 8. Else Print “It is not an Armstrong Number.”