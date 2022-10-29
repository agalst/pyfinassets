def test_different_dates(mocker):
    from pandas import DataFrame
    from pendulum import DateTime

    from assetfactory import FinancialAssetFactory
    from portfolio import Portfolio
    from position import Position

    assetFactory = FinancialAssetFactory()

    appleSecurity = assetFactory.create_asset(
        cfi_code="ESVUFR",
        name="Apple Inc. Common Stock (AAPL)",
        isin="US0378331005",
        mic="XNAS",
        symbol="AAPL",
    )
    mocker.patch(
        "pandas_datareader.get_data_yahoo", return_value=DataFrame({"Close": [155.74]})
    )

    myPortfolio = Portfolio()
    myApplePosition = Position(
        asset=appleSecurity, quantity=10, date=DateTime(2022, 10, 28)
    )
    myApplePosition1 = Position(
        asset=appleSecurity, quantity=10, date=DateTime(2022, 10, 29)
    )

    myPortfolio.addPosition(myApplePosition)
    myPortfolio.addPosition(myApplePosition1)
    myPortfolio.update_prices()
    assert myPortfolio.evaluate(date=DateTime(2022, 10, 28)) == 1557.4
