"""Blueprints for Jeans"""

class jeans():

    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print("Wearing the {} x {} {} jeans" .format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print("Removing the {} x {} {} jeans" .format(self.waist, self.length, self.color))
        self.wearing = False


def main():

    # instantiate the jeans object
    my_jeans = jeans(36,32, 'blue')
    my_jeans.wearing
    print(type(my_jeans))
    print(dir(my_jeans))

    # put on the jeans
    my_jeans.put_on()
    print(my_jeans.wearing)

    # remove the jeans
    my_jeans.take_off()
    print(my_jeans.wearing)

if __name__ == "__main__":
    main()

