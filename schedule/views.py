from django.shortcuts import render
from django.http import HttpResponse
from schedule import models
import datetime
# Create your views here.

def schedule(request):
    context = {}
    context['ip'] = get_ip(request)
    context['timeline'] = get_timeline()
    context['update_time'] = date2str(query_latest().sche_date)
    return render(request, 'schedule.html', context)

def get_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for#.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Build Time Line
def get_timeline():
    axis = []
    res = query_all()
    reslen = len(res)
    for i in range(0, reslen):
        axis.append(get_timeline_card(res[i].sche_date, \
                                        res[i].sche_title, \
                                        res[i].sche_content, \
                                        res[i].sche_rsc,
                                        i))
    return "\n".join(axis)

# Query Lastest Record
def query_latest():
    latest = models.schedule.objects.order_by('-sche_date').first()
    return latest

# Query All Records
def query_all():
    record_list = models.schedule.objects.order_by("-sche_date").all()
    return record_list

# Return Time Line Card
def get_timeline_card(date, title, content, rsc, idx):
    color = ['turqoise', 'black', 'bronw', 'indigo', 'purple', 'grey',
                'blue', 'red', 'orange', 'opal', 'green', 'pink']
    template = '<div class="timeline-post %s-post %s-trail"> \
    	<div class="timeline-meta"> \
    		<div class="meta-details">%s</div> \
    	</div> \
    	<div class="timeline-icon icon-dot"> \
    		<div class="timeline-bar"></div> \
    	</div> \
    	<div class="timeline-content" > \
    		<h2 class="content-title %s-title">%s</h2> \
    		<div class="content-details"> \
    			<p>%s</p> \
    			<a href=\"%s\">🔗</a> \
    		</div> \
    	</div><!-- timeline content --> \
    </div><!-- .timeline-post -->' % (color[idx%12], color[idx%12], date2str(date), color[idx%12], title, content, rsc)
    return template

def date2str(s):
    date_str = str(s)
    return date_str
