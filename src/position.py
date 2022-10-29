from pendulum import DateTime

from abstracts.abstractfinancialasset import AbstractFinancialAsset
from exceptions import SecurityQuotationMissingError
from quotation import SecurityQuotation


class Position:
    date: DateTime
    asset: AbstractFinancialAsset
    quantity: float
    securityQuotation: SecurityQuotation
    currencyLocal: str
    originalValueLocal: float
    marketValueLocal: float
    accruedInterest: float

    def __init__(
        self, asset: AbstractFinancialAsset, quantity, date: DateTime = DateTime.now()
    ):
        self.asset = asset
        self.quantity = quantity
        self.date = date
        self.securityQuotation = None

    def __str__(self):
        str_date = self.date.strftime("%Y-%m-%d")
        return f"On {str_date} {self.quantity} units of " + str(self.asset)

    def evaluate(self):
        if not self.securityQuotation:
            str_date = self.date.strftime("%Y-%m-%d")
            raise SecurityQuotationMissingError(
                f"Quotation for this security is not available on {str_date}"
            )
        self.marketValueLocal = self.securityQuotation.quotation * self.quantity
        return self.marketValueLocal
