from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import product_details
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import products,lovis1,shops,lovis2,AM_plasma
from django.db.models import Count

# Create your views here.


def home(request):
    products1= products.objects.all()
    shops_names = shops.objects.all()
    return render(request, 'first_page.html', {'products1': products1,'shops_names': shops_names})

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username already taken')
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('sign_up')
            else:

                user = User.objects.create_user(password=password1,username=user_name,email=email)
                user.save();
                print(" user created")
                return redirect('/home')
        else:
            messages.info(request, 'password not matching ')
            return redirect('sign_up')
    else:
        return render(request, 'testing1.html')

def sign_in(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid ')
            return redirect('sign_in')
    else:
        return render(request, 'testing1.html')
def sign_out(request):
    auth.logout(request)
    return redirect('home')

def details(request):

    a = str(request.GET["pid"])
    b = str(request.GET["sid"])
    c= str(request.GET["product"])


    if b =='none':
        products1 = products.objects.filter(id =int(a))
        products2 = shops.objects.all()

        return render(request, 'testing3.html', {'products1': products1,'products2': products2})

    elif a=='none':
        products1 = shops.objects.filter(id = int(b))
        for i in products1:
            shop = i.shop_name
        print('Lovis')
        tt = '.objects.all()'

        products2 = eval(shop+tt)
        group = 'products_name1'
        tt2 = '.objects.values(group).annotate(dcount=Count(group))'

        result = eval(shop+tt2)
        print(result)
        return render(request, 'testing3.html', {'products1': products1,'products2': products2,'data':result})

    elif a =='isproduct':
        products1 = shops.objects.filter(id=int(b))
        for i in products1:
            shop = i.shop_name
        print('Lovis')
        #products1.shop_name

        #products2 = lovis2.objects.filter(products_name1=c)
        #result = (lovis2.objects
        #          .values('products_name1')
        #         .annotate(dcount=Count('products_name1'))
        #          )

        tt = '.objects.filter(products_name1=c)'

        products2 = eval(shop + tt)
        group = 'products_name1'
        tt2 = '.objects.values(group).annotate(dcount=Count(group))'

        result = eval(shop + tt2)
        return render(request, 'testing3.html', {'products1': products1,'products2': products2,'data':result})


def test(request):
    pass

