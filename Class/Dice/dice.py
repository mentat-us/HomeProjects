import random
class Dice:
    def __init__(self):
        self.up_side = 0
        self.roll()

    def roll(self):
        self.up_side = random.randint(1,6)
        return self.up_side

class DiceSimulator:
    def __init__(self):
        self.__dice = Dice()
        self.__dice_count = 10
        self.__freq_list = []
        for i in range(0, 51):
            self.__freq_list.append(0)

    def simulate(self, N=100):
        tree = 0
        while(tree < N):
            trii = 0
            sum = 0

            while(trii < self.__dice_count):
                sum += self.__dice.roll()
                trii += 1

            self.__freq_list[sum - 10] += 1

            tree += 1

    def display(self):
        for i,val in enumerate(self.__freq_list, 10):
            print(i, ": ", val*"*")




ds = DiceSimulator()
ds.simulate(1000)
#ds.display()
#ds.simulate(10_000_000)
ds.display()


