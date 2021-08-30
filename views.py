from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import product_details
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import products,shops

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

    a = request.GET["id"]
    b = request.GET["id"]
    if a is not None:
        products1 = products.objects.filter(id = a)
        return render(request, 'testing3.html', {'products1': products1})
    elif b is not None:
        shop_names = shops.objects.filter(id = b)
        return render(request, 'testing3.html', {'shop_names':shop_names})
    else:
        return('home')


