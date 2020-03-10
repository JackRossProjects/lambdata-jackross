import random


class My_Class():
    """
    example class
    """

    def __init__(self, jacket_type, color, in_closet):
        """
        jacket_type (string) - the type of jacket
        color (string) - this jackets's color
        in_closet (int) - how many of this object in the closet
        """
        self.jacket_type = str(jacket_type)
        self.color = str(color)
        self.in_closet = int(in_closet)

    def check_closet(self):
        """
        checks whats in your closet
        """
        print('You have ' + self.color + ' ' + self.jacket_type + '. '+
              'There are ' + str(self.in_closet) + ' in your closet.')

    def go_shopping(self):
        """
        randomly picks a new color jacket
        """
        colors = ['green', 'blue']
        choice = random.randrange(len(colors))
        self.color = colors[choice]

    def how_many(self):
        """
        randomly picks an amount of jackets you purchased between 2 and 5 (inclusive)
        """
        self.in_closet = random.randrange(2,5)

