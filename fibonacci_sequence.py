# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# *1st 
# Time complexity: O(n)
# a= 0
# b =1
# for i in range(10):
#     print (a, end=", ")
#     c=a+b
#     a=b
#     b=c
# print ("...")

# *2nd Recursive Algorithm
# Time complexity: O(2^n)

# def fibonacci_recursive(n):
#     if n <=1:
#         return n
#     else:
#         return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

# num = int(input("Enter a number : "))
# for i in range(num):
#     print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")

# *3rd Optimized Recursive Algorithm (Memoization)
#  Time complexity: O(n)

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <=1:
        return n
    else:
        memo[n]= fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        # print(f"Memo of this function: {memo}")
        return memo[n]
        
    
number = 10
for i in range(number):
    print(f"Fibonacci({i}) = {fibonacci_memoization(i)}")

