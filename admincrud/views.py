from django.shortcuts import render
from metrics.models import Bitcoin_Price_Data

# Create your views here.
'''Retreives bitcoin price data from Metrics module and renders it for the view'''
def admincrud(request):
    """ A view to return the index page """
    btc = Bitcoin_Price_Data.objects.all()
    context = {
       
        'btc': btc,
        }

    return render(request, 'admincrud/admincrud.html', context)