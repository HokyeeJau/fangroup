from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.ytb, name='ytb'),
    url(r'download_bg/',  views.download_bg,  name="download_bg"),
    url(r'download_cm/',  views.download_cm,  name="download_cm"),
    url(r'download_ptr/', views.download_ptr, name="download_ptr"),
    url(r'download_thn/', views.download_thn, name="download_thn"),
]
