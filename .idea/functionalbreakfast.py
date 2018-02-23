"""A Functional Breakfast"""

cheese = 'cheddar'

def mix_and_cook():

    print("Mixing the ingredients")
    print("Greasing the pan")
    print("Pouring the mixture into the frying pan")
    print("cooking the first side")
    print("Flipping it")
    print("Cooking the second side")

def make_pancake():
    mix_and_cook()
    pancake = 'Enjoy the delicious {} pancake' .format(cheese)
    return pancake

def make_omelette():
    global cheese
    cheese = 'swiss'
    mix_and_cook()
    omelette = 'Enjoy the hearty {} omelette' .format(cheese)
    return omelette

def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omelette with {} ingredients, {}' .format(len(ingredients), ingredients)
    return omelette

def main():

    pancake = make_pancake()
    print(pancake)

    omelette = make_omelette()
    print(omelette)

    print(cheese)
    print(make_pancake())

    #bacon_omelette = fancy_omelette('bacon', 'cheese', 'sausage')
    #print(bacon_omelette)

if __name__ == "__main__":
    main()