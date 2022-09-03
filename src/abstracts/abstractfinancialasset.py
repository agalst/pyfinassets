from abc import ABC

class AbstractFinancialAsset(ABC):
    securityName: str
    securityISIN: str
    securityExchangeMIC: str