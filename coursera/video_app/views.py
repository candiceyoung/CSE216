from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist

def homepage(request):
    return render_to_response('homepage.html')
    # return HttpResponse("<p>Hello world</p>")
