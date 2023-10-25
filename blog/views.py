from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item

# Create your views here.


def get_blog_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'blog/blog_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_blog_list')
    else:
        form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add_item.html', context)
