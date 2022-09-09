from abc import ABC
from cficode import CFICode

class AbstractFinancialAsset(ABC):
    securityName: str
    securityISIN: str
    securityExchangeMIC: str
    securityCFICode : CFICode


