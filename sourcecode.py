import os
from django.conf import settings

# Set the settings module programmatically
os.environ['DJANGO_SETTINGS_MODULE'] = 'product_tracker.settings'

# Import Django settings after setting the environment variable
import django
django.setup()

# Now you can access your models or other Django functionality
#from products.models import Product
from products.task import fetch_coinbase_data  # Import the task function

fetch_coinbase_data()  # Run it like a normal function

# from pathlib import Path

# # This code simulates what you have in your settings.py
# base_dir = Path(__file__).resolve().parent
# print(__file__)
# print(base_dir)

# from products.task import fetch_coinbase_data

# fetch_coinbase_data.delay() 