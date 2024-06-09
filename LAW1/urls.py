from django.urls import path
from .views import *

urlpatterns =[
    path('',index_page, name='index_page'),
    path('about', about_us_page, name='about_us_page'),
    path('services', service_page, name='service_page'),
    path('lawyers', our_lawyers, name='our_lawyers'),
    path('why_us', why_us, name='why_us'),
    path('gallery', gallery_view, name='gallery_view'),
    path('team', team_view, name='team_view'),
    path('contact', contact_page, name='contact_page'),
]