from assets.financialassetdebt import FinancialAssetDebt
from assets.financialassetequity import FinancialAssetEquity
from cficode import CFICode


class FinancialAssetFactory:
    def create_asset(
        self, cfi_code: str = "", name: str = "", isin: str = "", mic: str = ""
    ):
        asset_cfi_code = CFICode(cfi_code)
        if asset_cfi_code.get_asset_class() == "Equity":
            return FinancialAssetEquity(
                name=name, isin=isin, cfi_code=asset_cfi_code, mic=mic
            )
        elif asset_cfi_code.get_asset_class() == "Debt":
            return FinancialAssetDebt(
                name=name, isin=isin, cfi_code=asset_cfi_code, mic=mic
            )
        else:
            raise NotImplementedError("This asset class is not implemented yet!")
