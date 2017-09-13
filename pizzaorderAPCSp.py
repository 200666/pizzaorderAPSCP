pizzalist = []
def menu():
    name = input('What is your name?')
    print('Hello', name)
    size = input('Would size of pizza would you like today? Type 1 for a full, and 2 for 1/2. ')
    if size == '1':
        pizzalist.append('full')
    elif size == '2':
        pizzalist.append('half')
        print(pizzalist)
    else:
        print("not an option! try again!")
    part2()

def part2():
    toppingslist = ['cheese 1', 'olives 2', "garlic 3"]
    print(toppingslist)
    toppings = input("What topping would you like on your pizza?")
    if toppings == '1':
       pizzalist.append("cheese")
       print(pizzalist)
    elif toppings == '2':
        pizzalist.append("olives")
        print(pizzalist)
    elif toppings == '3':
        pizzalist.append("garlic")
        print(pizzalist)
    else:
        print("not an option! try again!")

menu()

