from django.urls import path
from .views import priceoye_view,register_view, login_view,MobileImageView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('priceoye/', priceoye_view, name='priceoye'),
    path('register/', register_view, name='register'),  # Add this line
    path('login/', login_view, name='login'), 
    #  path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='priceoye'), name='logout'),  
    path('mobile/image/', MobileImageView.as_view(), name='mobile_image'), 
    path('contact/', views.contact_view, name='contact'), 
    path('about/', views.about_view, name='about'),
    path('faq/', views.faq, name='faq'),
    path('customer-service/', views.customer_service, name='customer_service'),
    

]
