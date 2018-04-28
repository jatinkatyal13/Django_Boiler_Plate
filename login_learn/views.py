from django.http import HttpResponse, HttpResponseRedirect

# authentication related stuff lives here
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import LoginForm

# Create your views here.

# @login_required
# def home(request):
#     return render(request, 'login_home.html')

class Home(TemplateView):
    template_name = 'login_home.html'

    @method_decorator(login_required) # we can use multiple decorators here
    def dispatch(self, request):
        return super().dispatch(request)

def login_view(request):
    login_error = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/login_learn')

    if request.method == "GET":
        loginForm = LoginForm()
    elif request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            # authenticate here
            user = authenticate(username = username, password = password)

            if user is not None:
                # user authenticated
                login(request, user)
                try:
                    next_page = request.GET['next']
                    return HttpResponseRedirect(next_page)
                except:
                    return HttpResponseRedirect('/login_learn')
            else:
                # wrong credentials
                login_error = "Username/Password incorrect"
    
    context = {
        'form' : loginForm,
        'login_error' : login_error
    }
    
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login_learn/login')