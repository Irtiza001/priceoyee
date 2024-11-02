from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('priceoye')  # Redirect to priceoye after successful login
    return render(request, 'myapp/login.html')

def priceoye_view(request):
    return render(request, 'myapp/priceoye.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., send an email, save to database, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # For demonstration, we will just return a success response
            # You can implement email sending logic here
            return HttpResponse(f"Thank you {name}, your message has been sent!")
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})


def about_view(request):
    return render(request, 'myapp/about.html')  # Adjust 'myapp' to match your app's name

def faq(request):
    return render(request, 'myapp/faq.html')  # Adjust 'myapp' to match your app's name

def customer_service(request):
    return render(request, 'myapp/customer_service.html')  # Adjust 'myapp' to match your app's name

<<<<<<< HEAD
=======
def career(request):
    return render(request, 'myapp/career.html')  # Render the careers.html template

def blog(request):
    return render(request, 'myapp/blog.html')  # Renders Press & Blog page

def term(request):
    return render(request, 'myapp/term.html')  # Renders Terms & Conditions page

def help(request):
    return render(request, 'myapp/help.html')  # Renders Help Center page

def privacy(request):
    return render(request, 'myapp/privacy.html')

def plan(request):
    return render(request, 'myapp/plan.html')

def activation(request):
    return render(request, 'myapp/activation.html')

def methods(request):
    return render(request, 'myapp/methods.html')









>>>>>>> 858ae1e (2nd week done)
#extra code

class MobileImageView(View):
    def get(self, request):
        return render(request, 'myapp/mobile_image.html')
    

    