##Improved version of the same function
def check_even_list(num_list):
    for x in num_list:
        if x % 2==0 :
            return True
        else:
            pass
    return False
##calling the function
print(check_even_list([1,3,5])) 
print(check_even_list([1,4,5]))
print(check_even_list([2,1,1,1]))
print(check_even_list([1,1,2]))


