from pendulum import DateTime
from position import Position

class Portfolio:
    positions: list[Position]
    portfolioDate: DateTime
    portfolioCurrencyBase: str

    def __init__(self):
        self.positions = []
        self.portfolioDate = DateTime.now()

    def __str__(self):
        result = "DATE         ISIN           QUANTITY   \n"
        for position in self.positions:
            result += self.portfolioDate.strftime("%Y-%m-%d") + "   " + position.asset.securityISIN + "   " + str(position.quantity)
        return result

    def addPosition(self, position: Position):
        if not position in self.positions:
            self.positions.append(position)
        else:
            raise Exception("This positon is already in the portfolio!")

    def modifyPosition(self):
        pass

    def removePosition(self):
        pass

    def evaluate(self):
        pass