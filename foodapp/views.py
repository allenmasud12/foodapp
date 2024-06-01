from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'item-form.html', {'form': form}) 

def update_item(request, id):
    item = Item.objects.get(id= id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id= id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'item-delete.html',{'item':item})