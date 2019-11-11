import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models



BASE_CRAIGSLIST_URL = 'https://chihuahua.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
# Create your views here.
def home(request):
	return render(request, 'base.html')

def promo(request):
	return render(request, 'my_app/promo.html')

def new_search(request):
	search = request.POST.get('search')
	models.Search.objects.create(search=search)
	final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
	response = requests.get(final_url)
	data = response.text
	soup = BeautifulSoup(data, features='html.parser')

	post_listings = soup.find_all('li', {'class': 'result-row'})
	
	final_postings = []
	for post in post_listings:
		post_titles = post.find(class_='result-title').text
		post_url = post.find('a').get('href')
		if post.find(class_='result-price'):
			post_price = post.find(class_='result-price').text
		else:
			post_price = "N/A"
		
		if post.find(class_= 'result-image').get('data-ids'):
			post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
			post_image_url = BASE_IMAGE_URL.format(post_image_id)
			print(post_image_url)
		else:	
			post_image_url = 'http://maestroselectronics.com/wp-content/uploads/2017/12/No_Image_Available.jpg'

		final_postings.append((post_titles, post_url, post_price, post_image_url))

	# print(post_titles)
	# print(post_price)
	# print(post_url)
	

	stuff_for_frontend = {
		'search': search,
		'final_postings': final_postings,
	}
	return render(request, 'my_app/new_search.html', stuff_for_frontend)