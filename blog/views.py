from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


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


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_blog_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'blog/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_blog_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_blog_list')
