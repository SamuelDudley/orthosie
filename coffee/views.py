from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from coffee.models import Coffee
from libs.printer_interface import Printer
from .forms import NameForm

from django.utils import timezone

def index(request):
    coffees = Coffee.objects.filter(orderDate__lte=timezone.now()).order_by('orderDate')
    context = {'coffees': coffees}
    return render(request, 'coffee/index.html', context)

def coffee_order(request):
    coffee= Coffee(freeText = 'this is a string', orderDate = timezone.now())
    coffee.save()
    #make a new object here
    #do something with it
    #push it to the display of the current order
    return redirect('index')

def no_sale(request):
    kick()
    return redirect('index')

def cancel_line(request, id):
    print id
    return redirect('index')
#     return render(request, 'coffee/'+str(id)+'.html')

def kick():
    printer = Printer(settings.PRINTER)#{'spool':'192.168.192.168', 'driver':'escpos', 'interface':'network'})#
    printer.kick_drawer()
    pass





# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             kick()
#             return HttpResponseRedirect('/thanks/')
# 
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
# 
#     return render(request, 'coffee/name.html', {'form': form})