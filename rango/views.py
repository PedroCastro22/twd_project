from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	context_dict = {'yourname': "Pedro Castro"}
	return render(request, 'rango/about.html', context=context_dict)
	#return HttpResponse("Rango says here is the about page. Click <a href='/rango/'>here</a> to go back to the main page.")
	