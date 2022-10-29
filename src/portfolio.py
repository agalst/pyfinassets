from pendulum import DateTime

from abstracts.abstractfinancialasset import AbstractFinancialAsset
from position import Position
from quotation import QuotationType
from yahoodataprovider import YahooDataProvider


class Portfolio:
    positions: list[Position]
    portfolioDate: DateTime
    portfolio_valuation = 0.0
    portfolioCurrencyBase: str

    def __init__(self):
        self.positions = []
        self.portfolioDate = DateTime.now()

    def __str__(self):
        result = "DATE         ISIN           QUANTITY           QUOTATION\n"
        for position in self.positions:
            result += (
                position.date.strftime("%Y-%m-%d")
                + "   "
                + position.asset.securityISIN
                + "   "
                + str(position.quantity)
                + "                 "
                + str(position.securityQuotation)
                + "\n"
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
        ydr = YahooDataProvider()

        for position in self.positions:
            position.securityQuotation = ydr.get_single_quotation(
                position=position, type=QuotationType.Close
            )
