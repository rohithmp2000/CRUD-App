from django.shortcuts import render,redirect
# from . forms import ProductsF orm
from . models import products

# Create your views here.

def index(request):
    data = products.objects.all()
    context = {
        'a' : data
    }
    # print(data)
    # print(context)
    return render(request,'index.html',context)

def add(request):
    if (request.method == 'POST'):
        Pname = request.POST.get('Pname')
        Price = request.POST.get('Price')
        Stock = request.POST.get('Stock')

        a = products(
            Pname = Pname,
            Price = Price,
            Stock = Stock,
        )
        a.save()
    return redirect('/index/')

def edit(request):
    data = products.objects.all()
    context = {
        'a' : data,
    }
    # print(context)
    return redirect('/index/',context)

def update(request,id):
    if (request.method == 'POST'):
        Pname = request.POST.get('Pname')
        Price = request.POST.get('Price')
        Stock = request.POST.get('Stock')

        a = products(
            id = id,
            Pname = Pname,
            Price = Price,
            Stock = Stock,
        )
        a.save()
        return redirect(index)
    return redirect(request,'/index/')

def delete(request,id):
    data = products.objects.filter(id = id).delete()
    context = {
        'a' : data
    }
    return redirect('/index/',context)

# ------------- Ali s way of doing ------------


# def add(request):
#     if(request.method == "POST"): 

#         form = ProductsForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             a=form.cleaned_data['Pname']
#             b=form.cleaned_data['Price']
#             c=form.cleaned_data['Stock']
            
#             d = products(Pname=a, Price=b, Stock=c)
#             d.save()
#             return HttpResponseRedirect('/Home')

#     else:
#         form = ProductsForm()
#         return render(request,'add.html',{'form': form})
