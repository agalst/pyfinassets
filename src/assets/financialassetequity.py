from abstracts.abstractfinancialasset import AbstractFinancialAsset

class FinancialAssetEquity(AbstractFinancialAsset):
    def __init__(self, name, isin, mic, cfi_code):
        self.securityCFICode = cfi_code
        self.securityExchangeMIC = mic
        self.securityISIN = isin
        self.securityName = name