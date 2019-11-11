from django.shortcuts import render, redirect
# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core import serializers
from cart.cart import Cart
from django.http import JsonResponse, HttpResponse
# Create your views here.
from shop.models import Product
 
# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'product_list'
    template_name = 'shop/index.html'
 
    def get_queryset(self):
        return Product.objects.all()
 
# view for the product entry page
# @login_required
class ProductEntry(CreateView):
    model = Product
    # the fields mentioned below become the entry rows in the generated form
    fields = ['product_title', 'product_price', 'product_desc', 'product_image']
 
# view for the product update page
# @login_required
class ProductUpdate(UpdateView):
    model = Product
    # the fields mentioned below become the entyr rows in the update form
    fields = ['product_title', 'product_price', 'product_desc', 'product_image']
 
# view for deleting a product entry
# @login_required
class ProductDelete(DeleteView):
    model = Product
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('shop:index')


#Shopping cart
def add_to_cart(request, product_id, quantity):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.add(product, product.product_price, quantity)
        subtotal = cart.summary()
        total_items = cart.count()
        return render(request, 'shop/cart.html', {'cart': Cart(request), 'subtotal': subtotal, 'total_items': total_items})
    else:
        return redirect('shop')
   

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        cart.remove(product)
        subtotal = cart.summary()
        total_items = cart.count()
        # data = {"results": {
        # "product title": product.product_title,
        # "product desc": product.product_desc
        # }}
        #return JsonResponse(data)
        return render(request, 'shop/cart.html', {'cart': Cart(request), 'subtotal': subtotal, 'total_items': total_items})
    else:
        return redirect('shop:index')
    

def get_cart(request):
    cart = Cart(request)
    subtotal = cart.summary()
    total_items = cart.count()
    return render(request, 'shop/cart.html', {'cart': Cart(request), 'subtotal': subtotal, 'total_items': total_items})

def get_products(request):
    products = Product.objects.all()
    product_list =serializers.serialize('json', products)
    # for product in product_list:
    #     data = {"Products":{
    #     "product_title": product.product_title,
    #     "product_desc": product.product_desc
    #     }}
    return HttpResponse(product_list, content_type="text/json-comment-filtered")

