from django.shortcuts import render, redirect, get_object_or_404
from app_GroceryBag import forms
from .models import GrossBag
from .forms import GrossBagForm


# Create your views here.

def View_Grocery_List(request):
    GroceryList = GrossBag.objects.all()
    return render(request, 'index.html', {'GroceryList': GroceryList})


def Add_Grocery_List(request):
    form = forms.GrossBagForm()
    if request.method == 'POST':
        form = forms.GrossBagForm(request.POST)
        print("Form Taken")
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('/')
    return render(request, 'add.html', {'from': form})


def Update_Grocery_List(request, id):
    record = GrossBag.objects.get(id=id)
    form = forms.GrossBagForm()
    if request.method == 'POST':
        form = forms.GrossBagForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.html', {'form':form,'record':record})


def delete_Grocery_List(request, id):
    GroceryList = GrossBag.objects.get(id=id)
    GroceryList.delete()
    return redirect('/')
