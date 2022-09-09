from pendulum import DateTime
from src.abstracts.abstractfinancialasset import AbstractFinancialAsset
from src.financialassetquotation import FinancialAssetQuotation

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
