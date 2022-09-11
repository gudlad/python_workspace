##Improved version
##return all the even numbers in the list
def check_even_list(num_list):
    # place holder variable for even no.
    evenlist=[]
    for x in num_list:
        if x % 2==0 :
            evenlist.append(x)
        else:
            pass
    return evenlist
##calling the function
print(check_even_list([1,2,3,4]))
print(check_even_list([1,4,5,6]))
print(check_even_list([2,1,1,1]))
print(check_even_list([1,1]))
