from django.shortcuts import get_object_or_404, redirect, render, reverse
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

def delete_date(request, date):
    get_object_or_404(Bitcoin_Price_Data, date=date).delete()
    return redirect(reverse('admincrud'))

# def edit_date(request, date):
#     get_object_or_404(Bitcoin_Price_Data, date=date).delete()
#     return render(request, 'admincrud/admincrud.html')