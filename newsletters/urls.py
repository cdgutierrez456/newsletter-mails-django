from django.urls import path
from .views import newsletter_signup, newsletter_unsubcribe

app_name = 'newletters'

urlpatterns = [
    path('singup/', newsletter_signup, name = 'optin'),
    path('unsubscribe/', newsletter_unsubcribe, name = 'unsubscribe')
]
