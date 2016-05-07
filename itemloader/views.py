from django.shortcuts import render
from django.http import Http404

from itemloader.models import Item

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request,'itemloader/index.html', {
        'items': items,
        })

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404("No luck, ducky")

    return render(request, 'itemloader/item_detail.html', {
        'item': item,
        })

