from pendulum import DateTime

from abstracts.abstractfinancialasset import AbstractFinancialAsset
from position import Position


class Portfolio:
    positions: list[Position]
    portfolioDate: DateTime
    portfolio_valuation = 0.0
    portfolioCurrencyBase: str

    def __init__(self):
        self.positions = []
        self.portfolioDate = DateTime.now()

    def __str__(self):
        result = "DATE         ISIN           QUANTITY   \n"
        for position in self.positions:
            result += (
                self.portfolioDate.strftime("%Y-%m-%d")
                + "   "
                + position.asset.securityISIN
                + "   "
                + str(position.quantity)
            )
        return result

    def addPosition(self, position: Position):
        if position not in self.positions:
            self.positions.append(position)
        else:
            raise Exception("This positon is already in the portfolio!")

    def modifyPosition(self):
        pass

    def removePosition(self, security: AbstractFinancialAsset) -> None:
        for i, position in enumerate(self.positions):
            if position.asset == security:
                self.positions.pop(i)
                return

    def evaluate(self, date: DateTime):
        for position in [x for x in self.positions if x.date == date]:
            self.portfolio_valuation += position.evaluate()
        return self.portfolio_valuation

    def update_prices(self):
        import pandas_datareader as pdr

        for position in self.positions:
            position.securityQuotation = pdr.get_data_yahoo(
                position.asset.securitySymbol,
                start=self.portfolioDate.strftime("%Y-%m-%d"),
                end=self.portfolioDate.strftime("%Y-%m-%d"),
            )["Close"].values[0]
