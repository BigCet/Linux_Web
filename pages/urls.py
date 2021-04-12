from django.urls import path

from .views import HomeView, ContactView, AboutView, ContactSendView

urlpatterns = [
    path('', HomeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/sent/', ContactSendView.as_view()),
    path('about/', AboutView.as_view()),


]