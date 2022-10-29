from pendulum import DateTime

from abstracts.abstractfinancialasset import AbstractFinancialAsset
from financialassetquotation import FinancialAssetQuotation


class Position:
    date: DateTime
    asset: AbstractFinancialAsset
    quantity: float
    securityQuotation: FinancialAssetQuotation
    currencyLocal: str
    originalValueLocal: float
    marketValueLocal: float
    accruedInterest: float

    def __init__(self, asset: AbstractFinancialAsset, quantity):
        self.asset = asset
        self.quantity = quantity
        self.date = DateTime.now()

    def __str__(self):
        return "On " + str(self.date) + f" {self.quantity} units of " + str(self.asset)

    def evaluate(self):
        self.marketValueLocal = self.securityQuotation * self.quantity
