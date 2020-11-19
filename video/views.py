from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def video(request):
    context = {}
    context['ip'] = get_ip(request)
    return render(request, 'video.html', context)

def get_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for#.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
