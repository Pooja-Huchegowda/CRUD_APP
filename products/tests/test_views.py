import pytest
from django.urls import reverse
from django.test import Client
from products.models import Product,HistoricalData
from products.forms import ProductForm

@pytest.mark.django_db
def test_product_list():
    # Create a product in the database
    product = Product.objects.create(ticker="BTC", name="Bitcoin")

    # Simulate a request to the 'product_list' view
    client = Client()
    response = client.get(reverse('product_list'))

    # Assert that the view renders successfully
    assert response.status_code == 200
    assert product.name in response.content.decode()
    assert 'historical_data' in response.context
    assert 'products' in response.context

@pytest.mark.django_db
def test_product_create():
    # Simulate a POST request to create a new product
    client = Client()
    response = client.post(reverse('product_create'), {'ticker': 'ETH', 'name': 'Ethereum'})

    # Assert that the product is created and we are redirected to the product list page
    assert response.status_code == 302
    assert Product.objects.filter(ticker='ETH').exists()

@pytest.mark.django_db
def test_product_update():
    # Create a product to be updated
    product = Product.objects.create(ticker="BTC", name="Bitcoin")

    # Simulate a POST request to update the product
    client = Client()
    response = client.post(reverse('product_update', kwargs={'pk': product.pk}), {'ticker': 'BTC', 'name': 'Bitcoin Updated'})

    # Assert that the product is updated and we are redirected to the product list page
    assert response.status_code == 302
    product.refresh_from_db()
    assert product.name == "Bitcoin Updated"

@pytest.mark.django_db
def test_product_delete():
    # Create a product to be deleted
    product = Product.objects.create(ticker="BTC", name="Bitcoin")

    # Simulate a request to delete the product
    client = Client()
    response = client.post(reverse('product_delete', kwargs={'pk': product.pk}))

    # Assert that the product is deleted and we are redirected to the product list page
    assert response.status_code == 302
    assert not Product.objects.filter(ticker="BTC").exists()

@pytest.mark.django_db
def test_product_list_ajax():
    # Create a product and some historical data
    product = Product.objects.create(ticker="BTC", name="Bitcoin")
    historical_data = HistoricalData.objects.create(
        product=product,
        timestamp='2025-02-14T01:00:00Z',
        open=3000.00,
        high=3100.00,
        low=2900.00,
        close=3050.00
    )

    # Simulate an AJAX request to the 'product_list' view
    client = Client()
    response = client.get(reverse('product_list'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    print(response.json())
    # Assert that the response is JSON and contains historical data
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert historical_data.product.ticker == product.ticker
