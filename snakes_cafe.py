import sys

welcome = """ 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
menu = """

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
asking_order = """
***********************************
** What would you like to order? **
***********************************
"""
print(welcome, menu)

items = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0,
    'salom' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden' : 0,
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0
}

while True:
    answer = input(asking_order)

    if answer == "quit":
        sys.exit()

    if answer in items:
        items[answer] +=1
        print(f'number of  {answer}', items[answer])
        print("Type 'quit' when you are done")

    else:
        print('not on menu')
