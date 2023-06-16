from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def category(request):
    return render(request, 'catalog/category.html')


def orders(request):
    return render(request, 'catalog/orders.html')


def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('text'))

    return render(request, 'catalog/contacts.html')
