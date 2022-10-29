from abc import ABC

from cficode import CFICode


class AbstractFinancialAsset(ABC):
    securityName: str
    securityISIN: str
    securityExchangeMIC: str
    securityCFICode: CFICode
    securitySymbol: str

    def __init__(self, name, isin, mic, cfi_code, symbol):
        self.securityCFICode = cfi_code
        self.securityExchangeMIC = mic
        self.securityISIN = isin
        self.securityName = name
        self.securitySymbol = symbol

    def __str__(self):
        return (
            "Security "
            + self.securityName
            + ", traded on "
            + self.securityExchangeMIC
            + " with ISIN "
            + self.securityISIN
        )
