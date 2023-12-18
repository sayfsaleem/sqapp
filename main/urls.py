from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='Home'),
    path('about/',views.AboutView.as_view(),name='About'),
    path('contact/',views.ContactView.as_view(),name='Contact'),
]
