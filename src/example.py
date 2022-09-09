from src.portfolio import Portfolio
from src.position import Position
from src.assetfactory import FinancialAssetFactory

assetFactory = FinancialAssetFactory()

appleSecurity = assetFactory.create_asset(cfi_code="", name="", isin="", mic="")

myPortfolio = Portfolio()
myApplePosition = Position(asset=appleSecurity, quantity=10)


myPortfolio.addPosition(myApplePosition)
print(myPortfolio)
