def even_check(number) :
    return number%2==0
print(even_check(int('21')))
print('\n')
##return true if any even number inside a list 
def check_even_list(num_list):
    for x in num_list:
        if x % 2==0 :
            return True
        else:
            pass
##calling the function
print(check_even_list([1,3,5])) # we are n't returning anything
print(check_even_list([1,4,5]))
print(check_even_list([2,1,1,1])) 
print(check_even_list([1,1,2]))
"""
 for x in num_list:
        if x % 2==0 :
            return True
        else:
            return False # this is wrong!!!
"""

