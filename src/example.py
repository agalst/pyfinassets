from portfolio import Portfolio
from position import Position
from assetfactory import FinancialAssetFactory

assetFactory = FinancialAssetFactory()

appleSecurity = assetFactory.create_asset(cfi_code="ESVUFR", name="Apple Inc. Common Stock (AAPL)", isin="US0378331005", mic="XNAS")

myPortfolio = Portfolio()
myApplePosition = Position(asset=appleSecurity, quantity=10)


myPortfolio.addPosition(myApplePosition)
print(myPortfolio)
print(myPortfolio.evaluate())
