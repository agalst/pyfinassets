from abc import ABC

from cficode import CFICode


class AbstractFinancialAsset(ABC):
    securityName: str
    securityISIN: str
    securityExchangeMIC: str
    securityCFICode: CFICode

    def __str__(self):
        return (
            "Security "
            + self.securityName
            + ", traded on "
            + self.securityExchangeMIC
            + " with ISIN "
            + self.securityISIN
        )
