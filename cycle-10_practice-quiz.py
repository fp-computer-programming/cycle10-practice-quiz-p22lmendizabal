# author: LM (AMDG) 1/27/22
# Question 1
def food_costs(groceries,costs): 
    #setting odified grocerie list and groceries equal to eachother
    groceries_mod = groceries
    #enumerate for loop and nested for loop to get to the list items
    for index, groups in enumerate(groceries):
        for groceries in groups:
            #getiing first value of costs list and grocery item then deleting the grocery price
            groceries_mod = "{0}: {1}".format(groceries, costs[0] )
            del costs[0]
            continue
    return groceries_mod



print(food_costs([['apple','pear','banana',],
    ['salmon','tuna','cod',],
    ['milk','eggs','yogurt']],
    [1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == ['apple: $1.99','pear: $2.99','banana: $0.99',],['salmon: $9.99','tuna: $10.99','cod:$6.99',],['milk: $3.49','eggs: $2.49','yogurt: $1.49'])

# Quesion 2
def factorial(number):
    #list is numbers up to the specified number
    lst_of_Numbers = list(range(1, number + 1))
    #for loop to iterate through list of numbers. Delete first value of list 
    for index, value in enumerate(lst_of_Numbers):
        value = lst_of_Numbers[0] * lst_of_Numbers[1]
        del lst_of_Numbers[0]
     
        return value

print(factorial(5))

#question 3
def fibonacci(number):
    #add new variables
    new_lst:[]
    counter = 0
    #for loo
    counter += 1
    counter += counter
    new_lst.append(counter)
    if counter > number:
        break
    return new_lst
        

