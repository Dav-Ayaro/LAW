from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import random, string
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class SiteRequirements():
    def __init__(self):
        pass

    def random_func(self, length):
        return ''.join([random.choice(string.ascii_letters + string.digits) for i in range (length)])
    
    def Time(self):
        return timezone.datetime.now().date()
    
class RenderUrls(SiteRequirements):
    def render_view(self, request, view_file, **kwargs):
        return render(request, view_file, kwargs)

    def redirection_func(self, redirect_path=None, **kwargs):
        if kwargs:
            redirect_path += '?' + urlencode(kwargs)
        return HttpResponseRedirect(reverse(redirect_path))
    
object = RenderUrls()

def index_page(request):
    return object.render_view(request, view_file='LAW1/index.html')

def about_us_page(request):
    return object.render_view(request, view_file='LAW1/about_us.html')

def service_page(request):
    return object.render_view(request, view_file='LAW1/services.html')

def our_lawyers(request):
    return object.render_view(request, view_file='LAW1/Team.html')

def why_us(request):
    return object.render_view(request, view_file='LAW1/why_us.html')

def gallery_view(request):
    return object.render_view(request, view_file='LAW1/gallery.html')

def team_view(request):
    return object.render_view(request, view_file='LAW1/team.html')

def contact_page(request):
    return object.render_view(request, view_file='LAW1/contact.html')