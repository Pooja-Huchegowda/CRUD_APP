import pytest
from django.utils.timezone import now
from products.models import Product, HistoricalData

@pytest.mark.django_db
def test_create_product(): # tests if a product instance is created successfully with all correct values
    """Test if a Product instance is created successfully."""
    product = Product.objects.create(ticker="BTC", name="Bitcoin")
    assert product.ticker == "BTC"
    assert product.name == "Bitcoin"
    assert str(product) == "Bitcoin"

@pytest.mark.django_db
def test_create_historical_data():
    """Test if a HistoricalData entry is created correctly and linked to a Product."""
    product = Product.objects.create(ticker="ETH", name="Ethereum")
    historical_data = HistoricalData.objects.create(
        product=product,
        timestamp=now(),
        open=3000.00,
        high=3100.00,
        low=2900.00,
        close=3050.00
    )

    assert historical_data.product == product
    assert historical_data.open == 3000.00
    assert historical_data.high == 3100.00
    assert historical_data.low == 2900.00
    assert historical_data.close == 3050.00
    assert str(historical_data).startswith("Eth")

