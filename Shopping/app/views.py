from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    d={}
    if request.method=='POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('cpassword')
        if p1==p2:
            try:
                usr = User.objects.create_user(username=u,email=e,password=p1)
                usr.save()
                
                profile = Profile(username=usr)
                profile.save()
                
                d['status1'] = f"Dear {u}, Register Successfully !!"
                return redirect('/login')
            except :
                d['status2'] = f"Dear {u},This email already exists !!"
        else:
            messages.warning(request,'Passwords do not match!!')
            return redirect('/signup')
        
    return render(request,'signup.html')

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        AOU = authenticate(username=username,password=password)
        
        if AOU and AOU.is_active:
            login(request,AOU)
            request.session['username']=username
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.warning(request,'Invalid Creadential!!')
            return redirect('/login')

    return render(request,'login.html')

def search(request):
    if request.method == 'POST':
        search_item = request.POST['search']
        product_item = Product.objects.filter(name__icontains=search_item)
    
    d={'Pro':product_item}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    return render(request,'search.html',d)

@login_required(login_url='login')
def profile(request):
    d={}
    if request.session.get('username'):
        username = request.session.get('username')
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    
    if request.method == 'POST':
        
        user.usernam=request.POST.get('username')
        p.address=request.POST.get('address')
        user.email=request.POST.get('email')
        if request.FILES:
            p.user_pic=request.FILES.get('img')

        user.save()
        p.save()
    
    return render(request,'profile.html',d)

def index(request):
    d = {}
    d['ALL'] = Category.objects.all()
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
        
    return render(request,'index.html',d)

def product_list(request,cat):
    category = Category.objects.get(category=cat)
    product = Product.objects.filter(category=category)
    d={'Pro':product}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    
    return render(request,'product.html',d)

def product_info(request,pk):
    d={'pro':Product.objects.get(pk=pk)}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p

    return render(request,'productinfo.html',d)

def signup(request):
    d={}
    if request.method=='POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('cpassword')
        if p1==p2:
            try:
                usr = User.objects.create_user(username=u,email=e,password=p1)
                usr.save()
                
                profile = Profile(username=usr)
                profile.save()
                
                d['status1'] = f"Dear {u}, Register Successfully !!"
                return redirect('/login')
            except :
                d['status2'] = f"Dear {u},This email already exists !!"
        else:
            messages.warning(request,'Passwords do not match!!')
            return redirect('/signup')
        
    return render(request,'signup.html')

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        AOU = authenticate(username=username,password=password)
        
        if AOU and AOU.is_active:
            login(request,AOU)
            request.session['username']=username
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.warning(request,'Invalid Creadential!!')
            return redirect('/login')

    return render(request,'login.html')


@login_required(login_url='login')
def cart(request,id):
    user = User.objects.get(username=request.user)
    obj = Product.objects.get(id=id)
    
    NWO,created = Product_cart.objects.get_or_create(user=user,name=obj)
    
    if created:
        NWO.ammount=obj.actual_price
        NWO.counter = 1
    else:
        NWO.counter += 1
        NWO.ammount=obj.actual_price*NWO.counter
    NWO.save()
    
    cart_list = Product_cart.objects.filter(user=user)
    m = 0
    for d in cart_list:
        m = m + (d.name.actual_price * d.counter)

    d={'cart':cart_list,'M':m}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    
    # return render(request,'cart.html',d)
    return redirect('/cart')

def cartall(request):
    user = User.objects.get(username=request.user)
    cart_list = Product_cart.objects.filter(user = user )
    m = 0
    for d in cart_list:
        m = m + (d.name.actual_price * d.counter)
    
    d={'cart':cart_list,'M':m}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p

    return render(request,'cart.html',d)


@login_required(login_url='login')
def qntysub(request,id):
    obj = Product.objects.get(id=id)
    meal = Product_cart.objects.get(user=request.user,name=obj)
    if meal.counter > 0:
        meal.counter -= 1
        meal.ammount -= obj.actual_price
        meal.save()
    Product_cart.objects.filter(counter=0).delete()
    
    return redirect('/cart')

@login_required(login_url='login')
def qntyadd(request,id):
    obj = Product.objects.get(id=id)
    meal = Product_cart.objects.get(user=request.user,name=obj)
    meal.counter += 1
    meal.ammount += obj.actual_price
    meal.save()
    
    return redirect('/cart')

@login_required(login_url='login')
def removedish(request,id):
    obj = Product.objects.get(id=id)
    Product_cart.objects.get(user=request.user,name=obj).delete()
    return redirect('/cart')

@login_required(login_url='login')
def order(request):
    user = User.objects.get(username=request.user)
    cart_list = Product_cart.objects.filter(user =user)
    m = 0
    actual = 0
    disc = 0
    for d in cart_list:
        m = m + (d.name.price * d.counter)
        actual = actual + (d.name.actual_price * d.counter)
        disc = disc + (d.counter * d.name.discount_price)
        
    Shipping_charge = 70.0
    ta = m + Shipping_charge-disc

    d={'order':cart_list,'am':m,'sc':Shipping_charge,'ta':ta,'disc':disc,"User":user,'p':actual}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    return render(request,'order.html',d)

@login_required(login_url='login')
def payment(request):
    user = User.objects.get(username=request.user)
    cartitem = Product_cart.objects.filter(user=user)
    for item in cartitem:
        Order_history(user=user,product=item.name,quantity=item.counter,amount=item.counter*item.name.actual_price).save()
        item.delete()
    return redirect('orderhistory')

@login_required(login_url='login')
def orderhistory(request):
    OH = Order_history.objects.filter(user=request.user)
    d={'OH':OH}
    if request.session.get('username'):
        username = request.session.get('username')
        
        user = User.objects.get(username=username)
        d['username']=user
        p =Profile.objects.get(username=user)
        d['pic']=p
    return render(request,'orderhistory.html',d)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
