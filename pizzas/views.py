from django.shortcuts import render, redirect
from .forms import *
from .models import *
from datetime import datetime, date

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizs(request):
    pizs = Pizza.objects.order_by()

    context = {'all_pizzas':pizs}
    # the key is the variable name you are going to use in the HTML file
    # the value is the variable name you are using in views.py
    return render(request, 'pizzas/pizs.html', context)

def pizza(request, pizza_name_id):
    pizza_name = Pizza.objects.get(id=pizza_name_id)
    toppings = Topping.objects.filter(pizza_name=pizza_name)
    acomment = Comments.objects.filter(pizza_name=pizza_name_id)
    image= Image.objects.filter(pizza_name=pizza_name_id)

    context = {'pizza_name':pizza_name, 'toppings':toppings, 'acomment':acomment,'image':image}

    return render(request, 'pizzas/pizza.html', context)



def comments(request, pizza_name_id):
    pizza_name = Pizza.objects.get(id=pizza_name_id)

    if request.method != 'POST':
        form = CommentsForm()
    else:
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            comments=form.save(commit=False)
            comments.pizza_name = pizza_name
            comments.save()
            return redirect('pizzas:pizza', pizza_name_id=pizza_name_id )

    context = {'form':form, 'pizza_name':pizza_name}

    return render(request,'pizzas/comments.html', context)