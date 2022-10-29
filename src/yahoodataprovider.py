import pandas_datareader as pdr

from position import Position
from quotation import QuotationType, SecurityQuotation


class YahooDataProvider:
    def __init__(self):
        pass

    def get_single_quotation(self, position: Position, type: QuotationType):
        r = pdr.get_data_yahoo(
            position.asset.securitySymbol,
            start=position.date.strftime("%Y-%m-%d"),
            end=position.date.strftime("%Y-%m-%d"),
        )
        date, high, low, openn, close, vol, adjclose = r.reset_index().values[0]
        match type:
            case QuotationType.Close:
                return SecurityQuotation(
                    timestamp=date, quotation=close, type=QuotationType.Close
                )
            case _:
                raise NotImplementedError("This quotation type is not implemented!")
