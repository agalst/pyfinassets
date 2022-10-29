# pyfinassets

Package to calculate the value of a portfolio of financial instruments

## Example

```
from pendulum import DateTime

from portfolio import Portfolio
from position import Position
from assetfactory import FinancialAssetFactory

assetFactory = FinancialAssetFactory()

appleSecurity = assetFactory.create_asset(cfi_code="ESVUFR",
                                          name="Apple Inc. Common Stock (AAPL)",
                                          isin="US0378331005",
                                          mic="XNAS",
                                          symbol="AAPL")

myPortfolio = Portfolio()
myApplePosition = Position(asset=appleSecurity, quantity=10, date=DateTime(2022,10,28))
myApplePosition1 = Position(asset=appleSecurity, quantity=10, date=DateTime(2022,10,3))


myPortfolio.addPosition(myApplePosition)
myPortfolio.addPosition(myApplePosition1)
myPortfolio.update_prices()
print(myPortfolio)
evaluation_date = DateTime(2022,10,4)
value = myPortfolio.evaluate(date=evaluation_date)
str_date = evaluation_date.strftime("%Y-%m-%d")
print(f"On {str_date} my portfolio is worth {value}$" )
```

To run the example `poetry run python src/example.py`
