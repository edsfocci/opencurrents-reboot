from django.conf.urls import url
from openCurrents import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='root'),

    # placeholders
    url(r'^$', views.HomeView.as_view(), name='login'),
    url(r'^process_signup/(?P<referrer>[\w\.@\+\-]*)$',
        views.HomeView.as_view(), name='process_signup'),
]
