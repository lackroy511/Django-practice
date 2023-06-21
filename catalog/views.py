from django.shortcuts import render

from catalog.models import Product, Contact

# Create your views here.


def index(request):
    
    products = Product.objects.all()[0:4]
    
    print(products)
    
    return render(request, 'catalog/index.html')


def categories(request):
    return render(request, 'catalog/category.html')


def orders(request):
    return render(request, 'catalog/orders.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('text')
        Contact.objects.create(name=name, email=email, massage=massage)
        
        data = {
            'name': name,
            'email': email,
            'massage': massage
        }
        
        return render(request, 'catalog/contacts.html', context=data)

    return render(request, 'catalog/contacts.html')
