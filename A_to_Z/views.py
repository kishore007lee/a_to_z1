from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import products,shops,trending_products
from django.db.models import Count

# Create your views here.


def home(request):
    products1= trending_products.objects.all()
    products2=products.objects.all()
    shops_names = shops.objects.all()


    return render(request, 'first_page.html', {'products1': products1,'shops_names': shops_names,'products2':products2})

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
    print(c)


    if b =='none':
        products1= products.objects.filter(id =int(a))
        products2 = shops.objects.all()

        return render(request, 'testing3.html', {'products1': products1,'products2': products2})

    elif a=='none':
        products1 = shops.objects.filter(id = int(b))
        for i in products1:
            shop = i.shop_name
        shop_id = b
        products2 = products.objects.filter(shop_id=int(b))
        result = []
        for i in products2:
            if i.product_name in result:
                pass
            else:
                result.append(i.product_name)


        return render(request, 'testing3.html', {'products1': products1,'products2': products2,'data':result})

    elif a =='isproduct':
        products1 = shops.objects.filter(id=int(b))
        for i in products1:
            shop = i.shop_name
        products2 = products.objects.filter(shop_id=int(b))
        result = []
        for i in products2:

            if i.product_name in result:
                pass
            else:
                result.append(i.product_name)
        products2 = products.objects.filter(product_name=c)



        return render(request, 'testing3.html', {'products1': products1,'products2': products2,'data':result})


def Add_cart(request):
    return render(request,'testing5.html')

