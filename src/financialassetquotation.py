from pendulum import DateTime

class FinancialAssetQuotation:
    price: float
    quotationTimestamp: DateTime

    def __init__(self, timestamp: DateTime, price: float):
        self.price = price
        self.quotationTimestamp = timestamp