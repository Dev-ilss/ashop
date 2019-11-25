from django.urls import path
from . import views

urlpatterns = [
	path('', views.topSearch, name='promo'),
	path('new_search', views.new_search, name='new_search'),
	path('products', views.get_products, name='products'),
	# path('promo', views.promo, name='promo'),
]