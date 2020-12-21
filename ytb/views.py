from django.shortcuts import render
from django.http import HttpResponse
from ytb.models import background, portrait, thumbnail, community
import locale
import datetime
import zipfile
import tempfile
import os
import io
from django.http import StreamingHttpResponse, HttpResponse
import zipstream
# locale.setlocale(locale.LC_CTYPE, 'chinese')
# Create your views here.

card_temp = "<div class=\"card col s12 m5\" style=\"margin-right: 10px\"> \
    <div class=\"card-image waves-effect waves-block waves-light card-hover\"> \
        <img class=\"activator\" src=\"{}\"> \
    </div> \
    <div class=\"card-content\"> \
        <span class=\"card-title activator grey-text text-darken-4\">{}<i class=\"material-icons right\">more_vert</i></span> \
        <p><a href=\"{}\" download>下载</a></p> \
    </div> \
    <div class=\"card-reveal\"> \
        <span class=\"card-title grey-text text-darken-4\">{}<i class=\"material-icons right\">close</i></span> \
        <p>{}</p> \
    </div> \
    <div class=\"card sticky-action\"> \
    </div>\n</div>" \

none_temp = "<div class=\"col s12 m5\">\
    <div class=\"card-panel teal card-hover\">\
        <span class=\"white-text\">暂时还没有管理员上传资源哦！\
        </span>\n</div>\n</div>"
rsc_root = 'static/rsc'

def ytb(request):
    context = {}
    context['ip'] = get_ip(request)
    context['background_pack'] = pack_background()
    context['portrait_pack'] = pack_portrait()
    context['thumbnail_pack'] = pack_thumbnail()
    context['community_pack'] = pack_community()
    return render(request, 'ytb.html', context)

# Download Images Zip
def download_thn(request):
    dir_name = 'thn'
    return zip_file(dir_name)

def download_cm(request):
    dir_name = 'cm'
    return zip_file(dir_name)

def download_ptr(request):
    dir_name = 'ptr'
    return zip_file(dir_name)

def download_bg(request):
    dir_name = 'bg'
    return zip_file(dir_name)

# Generate the html blocks
def pack_community():
    records = slice_community().values()
    pack = []
    if len(records) != 0:
        for i in range(len(records)):
            pack.append(card_temp.format('/static/rsc/'+records[i]['cm_image'],
                                        date_in_format(records[i]['cm_date']),
                                        '/static/rsc/'+records[i]['cm_image'],
                                        date_in_format(records[i]['cm_date']),
                                        records[i]['cm_content']))
    else:
        pack.append(none_temp)
    return "\n".join(pack)

def pack_thumbnail():
    records = slice_thumbnail().values()
    pack = []
    if len(records) != 0:
        for i in range(len(records)):
            pack.append(card_temp.format('/static/rsc/'+records[i]['thn_image'],
                                        date_in_format(records[i]['thn_date']),
                                        '/static/rsc/'+records[i]['thn_image'],
                                        date_in_format(records[i]['thn_date']),
                                        date_in_format(records[i]['thn_date'])))
    else:
        pack.append(none_temp)
    return "\n".join(pack)

def pack_portrait():
    records = slice_portrait().values()
    pack = []
    if len(records) != 0:
        for i in range(len(records)):
            pack.append(card_temp.format('/static/rsc/'+records[i]['ptr_image'],
                                        date_in_format(records[i]['ptr_date']),
                                        '/static/rsc/'+records[i]['ptr_image'],
                                        date_in_format(records[i]['ptr_date']),
                                        date_in_format(records[i]['ptr_date'])))
    else:
        pack.append(none_temp)
    return "\n".join(pack)

def pack_background():
    records = slice_background().values()
    pack = []
    if len(records) != 0:
        for i in range(len(records)):
            pack.append(card_temp.format('/static/rsc/'+records[i]['bg_image'],
                                        date_in_format(records[i]['bg_date']),
                                        '/static/rsc/'+records[i]['bg_image'],
                                        date_in_format(records[i]['bg_date']),
                                        date_in_format(records[i]['bg_date'])))
    else:
        pack.append(none_temp)
    return "\n".join(pack)

# The Sliced Lines of Query
def slice_community():
    records = query_community()
    return records[:2]

def slice_thumbnail():
    records = query_thumbnail()
    return records[:2]

def slice_portrait():
    records = query_portrait()
    return records[:2]

def slice_background():
    records = query_background()
    return records[:2]

# Query Complete Tables
def query_community():
    record_list = community.objects.order_by('-cm_date')
    return record_list

def query_thumbnail():
    record_list = thumbnail.objects.order_by('-thn_date')
    return record_list

def query_portrait():
    record_list = portrait.objects.order_by('-ptr_date')
    return record_list

def query_background():
    record_list = background.objects.order_by('-bg_date')
    return record_list

# Generate directory
def generate_dir(*args):
    return "/".join([*args])

# Turn datetime into String
def date_in_format(s):
    str2date = str(s)
    str2date = datetime.datetime.strptime(str2date, "%Y-%m-%d")
    date2str = datetime.datetime.strftime(str2date, "%Y年%m月%d日")
    date2str = str(date2str)
    return date2str

# Get IP
def get_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for#.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Zip Images
def zip_file(dir_name):
    zip_filename = dir_name+".zip"
    dir = generate_dir(rsc_root, dir_name)
    
    if os.path.isdir(dir):
        z = zipstream.ZipFile(mode='w', compression=zipfile.ZIP_DEFLATED)
        for f in os.listdir(dir):

            z.write(generate_dir(dir, f))
        response = StreamingHttpResponse(z, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename={}'.format(zip_filename)
        return response
    return HttpResponse("Sorry but Not Found the File")
