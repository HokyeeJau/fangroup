from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mng(request):
    context = {}
    return render(request, 'user-login.html', context)
