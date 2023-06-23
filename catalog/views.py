from django.shortcuts import render

from catalog.models import Product, Contact

# Create your views here.


def index(request):

    products = Product.objects.all()[0:3]
    context = {
        'products': products,
        'is_active_main': 'active'
    }
    return render(request, 'catalog/index.html', context=context)


def product(request, pk):
    
    item = Product.objects.get(pk=pk)
    
    context = {
        'name': item.name,
        'description': item.description,
        'image_preview': item.image_preview,
        'category': item.category,
        'price': item.price,
        'creation_date': item.creation_date,
        'update_date': item.update_date,
         
    }
    
    return render(request, 'catalog/product.html', context=context)



def categories(request):
    
    context = {
        'is_active_categories': 'active'
    }
    return render(request, 'catalog/categories.html', context=context)


def orders(request):
    
    context = {
        'is_active_orders': 'active'
    }
    return render(request, 'catalog/orders.html', context=context)


def contacts(request):
    
    context = {
        'is_active_contacts': 'active'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('text')
        Contact.objects.create(name=name, email=email, massage=massage)

        context = {
            'name': name,
            'email': email,
            'massage': massage,
            'is_active': 'active_contacts'
        }
        return render(request, 'catalog/contacts.html', context=context)
    return render(request, 'catalog/contacts.html', context=context)
