from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader
def index(request):
    list_item = Item.objects.all()
    # template =loader.get_template('index.html')
    context ={
        'item_list': list_item,
    }
    
    # return HttpResponse(template.render(context, request))
    return render(request,'index.html', context)
    

def item(request):
    return HttpResponse("this is two page")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item': item
    }
    return render(request, "detail.html", context)