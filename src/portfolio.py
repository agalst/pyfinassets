from pendulum import DateTime
from position import Position

class Portfolio:
    positions: list[Position]
    portfolioDate: DateTime
    portfolioCurrencyBase: str

    def __init__(self):
        self.positions = []

    def addPosition(self, position: Position):
        if not position in self.positions:
            self.positions.append(position)
        else:
            raise Exception("This positon is already in the portfolio!")

    def modifyPosition(self):
        pass

    def removePosition(self):
        pass