from assets.financialassetequity import FinancialAssetEquity

class FinancialAssetFactory:

    def create_asset(self, cfi_code: str="", name: str="", isin: str="", mic: str=""):
        if cfi_code.startswith("E"):
            return FinancialAssetEquity(name=name, isin=isin, cfi_code=cfi_code, mic=mic)