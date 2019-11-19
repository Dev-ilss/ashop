from django.urls import path
from . import views

urlpatterns = [
	path('', views.topSearch, name='promo'),
	path('new_search', views.new_search, name='new_search')
	# path('promo', views.promo, name='promo'),
]