from django.shortcuts import render
import time

def message(request):
    print("We are here")
    time.sleep(2)
    return render(request, 'core/items.html', {"items": [1,2,3,4,]})