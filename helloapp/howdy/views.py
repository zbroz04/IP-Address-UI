from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):

    def get(self, request, **kwargs):

    	myString = "This is a python string"

    	return render(request, 'index.html', { 'myString' : myString })