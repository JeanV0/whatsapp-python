from random import randrange
from random import randint


class Numbers:

    def __init__(self, quant) -> None:
        self.quant = quant
        self.numbers = []
        self.typeNumber = ["999", "981", "991"]

    def setDdd(self, ddd):
        if (type(ddd) == "int"):
            print('Error')
        else:
            self.ddd = ddd

    def generateNumbers(self):
        for x in range(1, self.quant):
            number = "55{}{}".format(self.ddd, self.typeNumber[randint(0, 2)])
            for x in range(6):
                random = randrange(0, 9)
                number = number + str(random)
            self.numbers.append(number)


    def getNumbers(self):
        return self.numbers
