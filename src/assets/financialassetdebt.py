from pendulum import DateTime
from abstracts.abstractfinancialasset import AbstractFinancialAsset

class FinancialAssetDebt(AbstractFinancialAsset):
    def __init__(self, name, isin, mic, cfi_code):
        self.securityCFICode = cfi_code
        self.securityExchangeMIC = mic
        self.securityISIN = isin
        self.securityName = name

    def accrue_interest(self, until_date: DateTime):
        pass

    def list_coupons(self):
        pass