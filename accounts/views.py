from django.shortcuts import render

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from accounts.models import LoginForm
# Create your views here. 

def login_user(request):
  logout(request)
  username = password = ''
  form = LoginForm(request.POST or None)

  if request.POST and form.is_valid():
    user = form.login(request)
    if user:
      login(request, user)
      return HttpResponseRedirect('/')
  return render(request, 'accounts/login.html', {'login_form': form })
  #return render_to_response('accounts/login.html', context_instance= RequestContext(request))  
  # if request.POST:
  #   username = request.POST['username']
  #   password = request.POST['password']
  #   user = authenticate(username=username, password=password)
  #   if user is not None:
  #     if user.is_active:
  #       login(request, user)
  #       return HttpResponseRedirect('/books/')
  #     else:
  #       error = "Invalid account"
  #   else:
  #     error = "Ivalid user / password combination"   
  # return render_to_response('accounts/login.html', context_instance= RequestContext(request))



