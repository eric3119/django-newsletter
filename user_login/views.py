from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from newsletter.views import ( NewsletterListView,)

# Create your views here.
class UserProfileView(LoginRequiredMixin, NewsletterListView):
    allow_empty=True
    template_name='user_profile.html'