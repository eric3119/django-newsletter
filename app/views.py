from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from newsletter.views import ( NewsletterListView, NewsletterDetailView,
    SubmissionArchiveIndexView, SubmissionArchiveDetailView,
    SubscribeRequestView, UnsubscribeRequestView, UpdateRequestView,
    ActionTemplateView, UpdateSubscriptionView,)

class UserProfileView(LoginRequiredMixin, NewsletterListView):
    allow_empty=True
    template_name='user_profile.html'

class NewsletterDetailView(LoginRequiredMixin, NewsletterDetailView):
    pass# template_name='newsletter_detail.html'

    