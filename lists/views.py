from django.shortcuts import render, redirect
from lists.models import Item, List
<<<<<<< HEAD
from lists.forms import ItemForm, ExistingListItemForm
=======
from lists.forms import ItemForm
>>>>>>> 8e1ed09cc2ce56ec4163fa9a79f9dcf0c912d4d7
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
<<<<<<< HEAD
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
=======
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
>>>>>>> 8e1ed09cc2ce56ec4163fa9a79f9dcf0c912d4d7
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
