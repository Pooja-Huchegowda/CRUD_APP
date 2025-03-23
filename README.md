To Run this application:

1.Install all the dependencies through requirement.txt file by running < "pip install -r requirement.txt" >

2.Launch the django application by running < "python  manage.py runserver">  and can view the UI by visiting "http://127.0.0.1:8000/"

3.For celery beat schedule :
    1.start redis by running  "brew services start redis"
    2.open a new terminal and start the celery worker node which will interact with the redis server  "celery -A product_tracker worker --loglevel=info"
    3.In a new terminal start the celery beat scheduler by running  "celery -A product_tracker beat --loglevel=info"

4.For running tests using pytest: "pytest products/tests/ --disable-warnings -v"



---------------------------------steps involved in this build------------------------------------
Created virtual environment myvenv

created django project product_tracker

created the django app products

Add django app "products" in settings.py under product_tracker

Run migrations to create the database models:
    python manage.py makemigrations products
    python manage.py migrate

After running migrations, check if the table exists in SQLite:
    python manage.py dbshell
    .tables

Created a json file productdata.json under products to add pre-defined bulk data into Product table

celery beat schedule to run the task(fetch_coinbase_api()) every hour using celery node and redis message b roker

product_list.html is used to create UI for product table and to show the historical data. added schedule to refresh UI every minute.
product_form.html is used for create and update operation of the product list(tickers)

Installed pytest and created test cases for models, views, urls

