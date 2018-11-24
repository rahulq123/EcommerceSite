
# Create your views here.
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, Member
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader







appname = 'Ecommerce'


# to tests whether user is logged in or not
def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'shop/not-logged-in.html', {})

    return test

# index view takes the request and displays the "shop/indext.html" page on the user browser
def index(request):
    context = {
        'appname': appname,
    }

    return render(request, 'shop/index.html', context   )

	
# login view takes the request of the username and checks using if statement if not in POST then return to "shop/login.html" page
# else it takes the username and password form the user and uses try and except with database to match the username 
# and if its correct than it sends back the reuest to "shop/login.html" page with appname, username and loggedin true
# else if the password is wrong than it display wrong password.

def login(request):
    if 'username' not in request.POST:
        return render(request, 'shop/login.html')
    else:
        u = request.POST['username']
        p = request.POST['password']
        try:
            member = Member.objects.get(pk=u)
        except Member.DoesNotExist:
            return HttpResponse("User does not exist")
        if p == member.password:
            request.session['username'] = u;
            request.session['password'] = p;
            return render(request, 'shop/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': True}
                          )
        else:
            return HttpResponse("Wrong password")


# singup view display the signup.html page on the browser
			
def signup(request):
    return render(request, 'shop/signup.html')

	
	
	
# register view takes the request post of the sign up page which used by the user register for the account
# than it shows in the Member database
# after storing, it sends the user to user-registered.html to display message to user that the registration has been successful.

def register(request):
    u = request.POST['username']
    p = request.POST['password']
    n = request.POST['name']
    e = request.POST['email']
    a = request.POST['address']
    ph = request.POST['phone']
    user = Member(username=u, password=p, name=n, email=e, address=a, phone=ph)
    user.save()
    context = {
        'appname': appname,
        'username': u
    }
    return render(request, 'shop/user-registered.html', context)


	
# logout view takes the username and checks whether is in request.session and its flushes to logs out the user and display the logout.html page 
# to the user to show the logout message
	
@loggedin
def logout(request):
    if 'username' in request.session:
        u = request.session['username']
        request.session.flush()
        context = {
            'appname': appname,
            'username': u
        }
        return render(request, 'shop/logout.html', context)
    else:
        raise Http404("Can't logout, you are not logged in")

# profile view display the user information such as; name, email, address and phone no

@loggedin
def profile(request):
    u = request.session['username']
    member = Member.objects.filter(pk=u).values()
    return render(request, 'shop/profile.html', {'users': member, 'loggedin': True})


# it verifies the username with database with the help of ajax in the template to check whether username is taken or available during the registration process

def regCheckUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:
            member = Member.objects.get(pk=u)
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; This username is taken</span>")
        except Member.DoesNotExist:
            return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")
    else:
        return HttpResponse("Expected 'username' in request")

# it verifies the username against the database with help of ajax in templates to check whether the username is valid or unknown during the login process

def logCheckUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:
            member = Member.objects.get(pk=u)
            return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")
        except Member.DoesNotExist:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Unknown username</span>")
    else:
        return HttpResponse("")


# it display the list of product on the browser
		
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
				   
				   
# it displays the details of the individual productto the user when browsing

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                    'cart_product_form': cart_product_form})