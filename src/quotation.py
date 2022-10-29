from enum import Enum

QuotationType = Enum(
    "QuotationType", ["Open", "Close", "Intraday", "Bid", "Low", "High"]
)


class SecurityQuotation:
    def __init__(self, timestamp, quotation, type: QuotationType):
        self.timestamp = timestamp
        self.quotation = quotation
        self.type = type

    def __str__(self):
        return "{:.2f}".format(self.quotation)
