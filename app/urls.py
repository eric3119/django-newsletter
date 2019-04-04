from django.urls import path, include
from .views import UserProfileView, NewsletterDetailView
from surlex.dj import surl

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),    
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    surl(
        '^<newsletter_slug:s>/$',
        NewsletterDetailView.as_view(), name='newsletter_detail'
    ),
]
