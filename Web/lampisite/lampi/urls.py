from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'lampi'

urlpatterns = [
    path('', cache_page(60*15)(views.IndexView.as_view()), name='index'),
    path('add/', cache_page(60*15)(views.AddLampiView.as_view()), name='add'),
    re_path(r'^device/(?P<device_id>[0-9a-fA-F]+)$',
            cache_page(60*15)(views.DetailView.as_view()), name='detail'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
]
