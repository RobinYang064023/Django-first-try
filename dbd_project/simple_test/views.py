from django.shortcuts import render
from datetime import datetime

# Create your views here.



def display(request):
    return render(request, 'show_funsionTable.html', {
        'current_time': str(datetime.now()),
    })
def simple_test(request):
    return render(request, 'simple_test.html', {
        'current_time': str(datetime.now()),
    })
def data_collection(request):
    return render(request, 'data_collection.html', {
        'current_time': str(datetime.now()),
    })
def data_visualization(request):
    return render(request, 'data_visualization.html', {
        'current_time': str(datetime.now()),
    })