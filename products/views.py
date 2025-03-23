from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, HistoricalData
from .forms import ProductForm

def product_list(request):  #read
    products = Product.objects.all()
    #historical_data = HistoricalData.objects.all()
    historical_data = HistoricalData.objects.order_by('-timestamp')[:1000]
    print(f"Products: {products}")
    print(f"Historical Data: {historical_data}")
    #refresh_time = timezone.now()
    # if request.is_ajax():  # If the request is AJAX, return data in JSON format
    #     historical_data_list = list(historical_data.values('product', 'timestamp', 'open', 'high', 'low', 'close'))
    #     return JsonResponse(historical_data_list, safe=False)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        historical_data_list = list(historical_data.values('product', 'timestamp', 'open', 'high', 'low', 'close'))
        return JsonResponse(historical_data_list, safe=False)

    return render(request, 'product_list.html', {'products': products, 'historical_data': historical_data})

def product_create(request):   #create
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):  #update
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):    #delete
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')

