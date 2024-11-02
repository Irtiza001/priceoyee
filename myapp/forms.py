from django import forms
from .models import BlogPost
from .models import Service
from .models import Profile

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_image']
