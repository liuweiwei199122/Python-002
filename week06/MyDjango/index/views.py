from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import T1

def index(request):

	comment = T1.objects.filter(n_star__gt=3)[:20]
	return render(request, 'index.html', locals())


