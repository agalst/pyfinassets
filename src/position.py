from pendulum import DateTime
from src.abstracts.abstractfinancialasset import AbstractFinancialAsset

class Position:
    date: DateTime
    security: AbstractFinancialAsset
    quantity: float
    securityQuotation: FinancialAssetQuotation
    currencyLocal: str
    originalValueLocal: float
    marketValueLocal: float
    accruedInterest: float

    def __init__(self):
        pass
