import requests
from celery import shared_task
from products.models import Product, HistoricalData
from datetime import datetime, timezone, timedelta
#from celery.decorators import periodic_task

COINBASE_API_URL= "https://api.exchange.coinbase.com/products/{}/candles?granularity=3600"
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(hours=1)
start_time_str = start_time.isoformat()  # Example: 2025-01-01T00:00:00
end_time_str = current_time.isoformat() 
params = {
    'start_time': start_time_str,
    'end_time': end_time_str,
    'granularity': 3600
}
cutoff_date = datetime(2025, 2, 10)
HistoricalData.objects.filter(timestamp__lt=cutoff_date).delete()
@shared_task
def fetch_coinbase_data():
    products = Product.objects.all()

    for product in products:
        #print(product.ticker)  #change
        response = requests.get(COINBASE_API_URL.format(product.ticker), params=params)
        data = response.json()
        #print(response.status_code)

        if data:
            for entry in data:
                #print(entry)
                try:
                    timestamp = datetime.fromtimestamp(entry[0], tz=timezone.utc)
                    low, high, open_, close = entry[1:5]
                    #print(timestamp)
                    HistoricalData.objects.create(
                        product=product,
                        timestamp=timestamp,
                        open=open_,
                        high=high,
                        low=low,
                        close=close
                    )
                except Exception as e:
                    print(f"Error saving data for {product.ticker} at {timestamp}: {e}")
                    continue
