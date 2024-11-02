from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm
from .models import BlogPost
from .forms import BlogPostForm
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('priceoye')  # Redirect to priceoye after successful login
#     return render(request, 'myapp/login.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'myapp/profile.html', {'form': form})



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

# def customer_service(request):
    # return render(request, 'myapp/customer_service.html')  # Adjust 'myapp' to match your app's name


# Read (List all services)
def service_list(request):
    services = Service.objects.all()
    return render(request, 'myapp/service_list.html', {'services': services})

# Create
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            services = Service.objects.all()
            return render(request, 'myapp/service_list.html', {'services': services})
    else:
        form = ServiceForm()
    return render(request, 'myapp/service_form.html', {'form': form})

# Update
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            services = Service.objects.all()
            return render(request, 'myapp/service_list.html', {'services': services})
    else:
        form = ServiceForm(instance=service)
    return render(request, 'myapp/service_form.html', {'form': form})

# Delete
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        services = Service.objects.all()
        return render(request, 'myapp/service_list.html', {'services': services})
    return render(request, 'myapp/service_confirm_delete.html', {'service': service})





def career(request):
    return render(request, 'myapp/career.html')  # Render the careers.html template

def blog(request):
    return render(request, 'myapp/blog.html')  # Renders Press & Blog page

# List all blog posts (Read)
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/blog_list.html', {'posts': posts})

# Create a new blog post
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            posts = BlogPost.objects.all()
            return render(request, 'myapp/blog_list.html', {'posts': posts})
    else:
        form = BlogPostForm()
    return render(request, 'myapp/blog_form.html', {'form': form})

# Update an existing blog post
def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            posts = BlogPost.objects.all()
        return render(request, 'myapp/blog_list.html', {'posts': posts})
    
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'myapp/blog_form.html', {'form': form})

# Delete a blog post
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        posts = BlogPost.objects.all()
        return render(request, 'myapp/blog_list.html', {'posts': posts})
    return render(request, 'myapp/blog_confirm_delete.html', {'post': post})












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









#extra code

class MobileImageView(View):
    def get(self, request):
        return render(request, 'myapp/mobile_image.html')
    

    