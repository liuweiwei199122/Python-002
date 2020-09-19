from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import T1
from . import form
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def index(request):

	comment = T1.objects.filter(n_star__gt=3)[:20]
	return render(request, 'index.html', locals())


def login(request):
	login_form = form.LoginForm()
	return render(request, 'login.html', locals())

def login2(request):
	if request.method == 'POST':
		login_form = form.LoginForm(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user:
				return redirect('index')
			else:
				return HttpResponse('用户名或密码错误')

	if request.method == 'GET':
		login_form == form.LoginForm()
		return render(request, 'login.html', locals())