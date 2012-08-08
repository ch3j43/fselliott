from django.template.context import RequestContext
from fselliott.forms import LogInForm
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def auth_login(request):
    context_instance = RequestContext(request) 

    if request.user.is_authenticated():
        return redirect('home')

    info = {}
    form = LogInForm()    

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username/Password is incorrect.')
    
    info['form'] = form
    return render_to_response('auth/login.html',info, context_instance)

def auth_logout(request):
    if request.user.is_authenticated():
        logout(request)
        messages.success(request, 'Successfully Logged out. ')
    
    return redirect('login')