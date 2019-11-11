from django.conf.urls import url
 
from shop import views
 
app_name = 'shop'
 
urlpatterns = [
 
    # /shop/
    url(r'^$', views.IndexView.as_view(), name='index'),
 
    # shop/product/entry
    url(r'^product/entry/$',views.ProductEntry.as_view(),name='product-entry'),
 
    # shop/product/2
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),
 
    # shop/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete'),
    # add to cart shop/product/(?P<pk>[0-9]+)/add
    url(r'^add/(?P<product_id>\w+)/(?P<quantity>\d{1,10})$', views.add_to_cart, name='add_to_cart'),
    #get cart items
    url(r'^cart/$', views.get_cart, name='get_cart'),
    #remove from cart
    url(r'^remove/(?P<product_id>\w+)/$', views.remove_from_cart, name='remove_from_cart'),

    url(r'^products/$',views.get_products,name='get_products')
 
]