from django import forms
from .models import NewsletterUser, NewsLetter

class NewsLetterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']
        
class NewLetterCreationForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['name', 'subject', 'body', 'email']