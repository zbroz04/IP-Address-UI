import socket

from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .forms import IPAddress

def home(request):

	if request.method == 'POST':

		form = IPAddress(request.POST)

		if form.is_valid():
			get_URL = form.cleaned_data['ip_address']
			convert_URL_to_IP = socket.gethostbyname(get_URL)
			print(convert_URL_to_IP)
			return render(request, 'search/home.html', { 'display_ip_address' : convert_URL_to_IP} )
		else:
			return render(request, 'search/home.html', { 'display_ip_address' : "URL Invalid"} )
	else:
		form = IPAddress()

	return render(request, 'search/home.html')