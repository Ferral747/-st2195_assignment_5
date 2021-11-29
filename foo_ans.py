# def is_divisible_by_k(x, k):
#     '''
#     Checks whether x is divisible by k.
#     '''                       # assert is not used to return value back to caller
#     assert x%k == 0           # assert is used to debug code, it stops everytime x % k not equal to 0

def is_divisible_by_k(x, k):
    '''
    Checks whether x is divisible by k.
    '''
    return x % k == 0

# '''
# Store all the integers that are multiples of 2 or 5 or 7 
# that are lower or equal to 1000
# '''
# x = ()                        # x is assigned as an empty tuple, tuple is immutable
# for i in range(1000):         # i will have range from 0 to 999
#                                                                   # wrong input argument '3' instead of '5', 'x' variable should be 'i'
#     if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) |      # syntax for ('and','&'), ('or','|') is incorrect, wrong input argument of '3'
#         is_divisible_by_k(x, 7):                                  # Boolean logic is wrong, and extra parenthesis
#                                                                   # invalid syntax to continue in next line, '\' should be used
#     x.append(i)                       # tuple is immutable, cannot store any elements
#                                       # wrong indentation

'''
Store all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000
'''
nums = []
for x in range(1, 1001):
    if is_divisible_by_k(x, 2) or is_divisible_by_k(x, 5) or is_divisible_by_k(x, 7):
        nums.append(x)

# '''
# Sum all the integers that are multiples of 2 or 5 or 7 
# that are lower or equal to 1000 (excluding doubles)
# '''
# sum(x)                        # x is empty, sum will be zero

'''
Sum all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
sum(nums)                       # 328927 printed
