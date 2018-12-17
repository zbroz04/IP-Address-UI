from django import forms


class IPAddress(forms.Form):
    ip_address = forms.URLField()