from django.urls import path
from .views import priceoye_view, MobileImageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('priceoye/', priceoye_view, name='priceoye'),
    # path('register/', register_view, name='register'),  # Add this line
    # path('login/', login_view, name='login'), 
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    # path('logout/', auth_views.LogoutView.as_view(next_page='priceoye'), name='logout'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),


    path('mobile/image/', MobileImageView.as_view(), name='mobile_image'), 
    path('contact/', views.contact_view, name='contact'), 
    path('about/', views.about_view, name='about'),
    path('faq/', views.faq, name='faq'),
   
    # path('customer-service/', views.customer_service, name='customer_service'),
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/update/<int:pk>/', views.service_update, name='service_update'),
    path('services/delete/<int:pk>/', views.service_delete, name='service_delete'),


    path('career/', views.career, name='career'),  # Define URL for careers page
   
    # path('blog/', views.blog, name='blog'),
    path('blog_list', views.blog_list, name='blog_list'),           # List all blog posts
    path('new/', views.blog_create, name='blog_create'),    # Create a new blog post
    path('<int:pk>/edit/', views.blog_update, name='blog_update'),  # Update a blog post
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'), # Delete a blog post

    
    path('term/', views.term, name='term'),
    path('help/', views.help, name='help'),  # Help Center page URL
    path('Privacy/', views.privacy, name='Privacy'),        # Privacy Policy page
    path('plans/', views.plan, name='plans'), # Installments Plan page
    path('activation/', views.activation, name='activation'), # E-Warranty Activation page
    path('methods/', views.methods, name='methods'),

]
