from pendulum import DateTime
from src.abstracts.abstractfinancialasset import AbstractFinancialAsset

class FinancialAssetBond(AbstractFinancialAsset):
    def __init__(self):
        pass

    def accrue_interest(self, until_date: DateTime):
        pass

    def list_coupons(self):
        pass