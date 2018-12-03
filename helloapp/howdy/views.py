import socket

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):

    def get(self, request, **kwargs):

    	hostName = ['www.google.com', 'www.yahoo.com', 'www.abcnews.com']

    	hostIP = [
    				hostName[0] + " : " + socket.gethostbyname('www.google.com'),
    			 	hostName[1] + " : " + socket.gethostbyname('www.yahoo.com'),
    				hostName[2] + " : " + socket.gethostbyname('www.abcnews.com')
    			 ]

    	#myString = "This is a python string"

    	return render(request, 'index.html', { 'hostAddress' : hostIP })