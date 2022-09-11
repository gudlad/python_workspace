work_hours=[('Abby',100),('Billy',4000),('Cassie',800)]
##finding the employee of the month

def employee_check(work_hours) :
##    placeholder variables
    current_max=0
    employee_of_month=''
##    we do some tuple unpacking in the for loop
    for employee,hours in work_hours :
        if hours>current_max :
            current_max=hours
            employee_of_month=employee
        else :
            pass
##     return
    return (employee_of_month,current_max)


result=employee_check(work_hours)
print(result)
print('\n')
##As the returned result contains 2 values we can also
##unpack the returned result
'''
name,hours=employee_check(work_hours)
print(name)
print(hours)
'''
name,hours=result
print(name)
print(hours)
