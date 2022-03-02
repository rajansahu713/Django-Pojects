from django.urls import path

from userapi.models import UserDetails
from .views import UserDetailsViews,BankingView
urlpatterns = [
    path('user/',UserDetailsViews.as_view()),
    path('banking/',BankingView.as_view()),
]