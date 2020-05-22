import Class.Coin.coin as coin
class CoinProb:
    def __init__(self):
        self.coin = coin.Coin(coin.Coin.HEAD)
        self.prob = 0

    def simulate(self, times=1000):
        head_counter = 0
        for i in range(times):
            self.coin.flip()
            cur = self.coin.get_face()
            if cur == coin.Coin.HEAD :
                head_counter += 1

        self.prob = head_counter / times


    def __str__(self):
        return str(self.prob)



prob = CoinProb()
prob.simulate()
print(prob)

prob.simulate(100_000)
print(prob)

prob.simulate(1_000_000)
print(prob)

prob.simulate(10_000_000)
print(prob)
