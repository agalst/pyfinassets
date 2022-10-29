from pendulum import DateTime

from abstracts.abstractfinancialasset import AbstractFinancialAsset


class FinancialAssetDebt(AbstractFinancialAsset):
    def accrue_interest(self, until_date: DateTime):
        pass

    def list_coupons(self):
        pass
